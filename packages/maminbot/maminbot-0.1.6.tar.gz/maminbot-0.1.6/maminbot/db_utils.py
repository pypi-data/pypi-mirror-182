"""Utilities for interacting with our cloud db (Deta Base - not a typo).
"""
import builtins
from collections import deque
import pandas as pd
from datetime import datetime
from deta import Deta
import json
from pathlib import Path
import warnings

# pd_tools makes coalesce available
from htools import tolist, pd_tools, random_str
from maminbot import config as cfg


def collapse_related_docs(chunk, concat_col='text', sep='\n'):
    if chunk.shape[0] <= 1:
        return chunk.reset_index(drop=True)
    nested_row = {
        col: sep.join(chunk[col].tolist()) if col == concat_col
        else chunk[col].values[0]
        for col in chunk.columns
    }
    # Don't use from_dict because that converts lists of 1 back into
    # primitives.
    return pd.DataFrame([nested_row])


def fetch_records(user='', tags=(), tag_strategy='any', prompt_contains='',
                  text_contains='', db=None, collapse=True, **kwargs):
    """Fetch records from Deta Base maminbotDB.

    Parameters
    ----------
    user: str
        Optionally provide one of the names in maminbot.config.users to only
        retrieve text from that user.
    tags: list[str]
        Optionally provide one or more tags to look for. Depending on tag
        strategy, you can choose to keep only rows that contain all tags or
        keep rows that contain any of the specified tags.
    tag_strategy: str
        "any" or "all". "any" returns rows that contain any of the tags the
        user passed in, while "all" requires rows to possess all specified tags
        in order to be returend.
    prompt_contains: str
        If provided, we only return rows where the "prompt" columnn contains
        the specified text. Case insensitive. Rows with no prompt will never be
        returned.
    text_contains: str
        If provided, we only return rows where the "text" columnn contains the
        specified text. Case insensitive.
    db: deta.base._Base
        Deta Base object. Typically created by
        `deta.Deta(project_key).Base(project_name)` where project_name is
        "maminbotDB".
    collapse: bool
        If True, any docs that were stored from a single piece of input text
        will be combined back into one row. Notice how in store_record in this
        same module, we have to do this for long docs (>50k characters) to
        avoid Deta http errors.
    kwargs: any
        Ignored - just makes it easier to pass in all DataTrainingArguments
        in s00 and maminbot.datasets.LanguageModelDataset.

    Returns
    -------
    pd.DataFrame
    """
    if not db:
        db = connect_db()
    query = {}
    if user:
        query['user'] = user
    tags = tolist(tags)
    if tags and tag_strategy not in ('any', 'all'):
        raise ValueError(f'Got unexpected tag_strategy {tag_strategy}. '
                         f'Should be "any" or "all".')
    res = db.fetch(query).items
    df = pd.DataFrame(res)
    if tags:
        func = getattr(builtins, tag_strategy)
        df = df[df.tags.apply(lambda x: func(tag in x for tag in tags))]
    if prompt_contains:
        df = df[df.prompt.str.lower().str.contains(prompt_contains.lower())]
    if text_contains:
        df = df[df.text.str.lower().str.contains(text_contains.lower())]
    df['dt'] = pd.to_datetime(df.dt)
    if collapse and 'doc_id' in df.columns:
        df['doc_id'] = df.coalesce(['doc_id', 'key'])
        cols = df.columns.drop('doc_id').tolist()
        df = df.sort_values('dt', ascending=True)\
            .groupby('doc_id')[cols]\
            .apply(collapse_related_docs)
    return df.reset_index(drop=True)


def load_creds(secrets=None):
    """
    Output isn't actually mutated but streamlit always raises a warning here
    unless we allow output mutation.
    NOTE: debug must be after st.cache. Do NOT use htools.decorate_functions
    because then debug will be on the outside and caching won't work.
    """
    if secrets:
        return dict(secrets.deta_creds)
    try:
        df = pd.read_csv(cfg.root/'data/creds/deta.csv')
        return df.to_dict(orient='records')[0]
    except FileNotFoundError:
        # This is how we load creds on saturn cloud. We made this available
        # by calling load_creds locally, passing that to json.dumps() and
        # copy-pasting it into a saturn secret. Then we attached that secret
        # to the relevant gpu resource as a file at the path below.
        with open(Path('~/secrets/deta_creds').expanduser(), 'r') as f:
            return json.load(f)


def connect_db(project_key='', project_name='', **kwargs):
    """Load deta.Base object that can be used to fetch items from our cloud
    database.

    Parameters
    ----------
    project_key: str
        Deta "project_key". Should not expose this on github.
    project_name: str
        Deta "project_name". This doesn't need to be private.
    kwargs: any
        Extra kwargs are ignored. Just makes it so streamlit secrets is less
        brittle - we can include all deta creds without worrying about which
        args are necessary.

    Returns
    -------
    deta.base._Base
    """
    if not (project_key and project_name):
        kwargs.update(DETA_CREDS)
        project_key = kwargs['project_key']
        project_name = kwargs['project_name']
        warnings.warn(f'Missing key and/or name so defaulting to '
                      f'{project_name} project creds.')
    for obj in (project_key, project_name):
        if not isinstance(obj, str) or obj[0] == '{':
            raise ValueError(
                'Input args should be strings. It looks like you might have '
                f'passed in a dict or stringified dict by accident: {obj}'
            )
    deta = Deta(project_key)
    return deta.Base(project_name)


def store_record(db, user, prompt_type, prompt, tags, text, _internal=False,
                 doc_id=''):
    """Add a record to the maminbotDB Deta Base, chunking it up into multiple
    docs if necessary since Deta Base errors out once we hit ~70k characters.

    Parameters
    ----------
    db: deta.base._Base
        Obj returned by connect_db(), for example.
    user: str
        One of maminbot.config.users, e.g. 'adrienne'. This will be
        auto-lowercased.
    prompt_type: str
        Dev-friendly prompt name, usually a gpt task name. One of
        ("misc_writing_prompt_ideas",
         "journal_entry_ideas",
         "creative_writing_ideas").
    prompt: str
        Text prompt that inspired the written text. 'n/a' will be considered
        to be no prompt (stored as empty str).
    tags: list[str]
        Let users provide tags to make it easier to train task-specific models
        later.
    text: str
        The user-provided piece of writing.
    _internal: bool
        User should never pass this in explicitly. The function uses this to
        differentiate between user calls and recursive calls, which occur when
        the provided text is too long to store in a single Deta doc.
    doc_id: str
        User shouldn't specify this manually. It helps us store very long
        documents in multiple Deta docs (because they produce an http error
        otherwise) that can later be reconstructed into the original doc if
        desired.

    Returns
    -------
    list[dict]: each dict corresponds to one doc that was added to the db.
    This includes a newly generated PK 'key' field. A long piece of input text
    can end up generating many docs, but anything <50k characters will be kept
    in a single doc.
    """
    doc_id = doc_id or random_str(10)
    user = user.lower()
    if prompt.lower() == 'n/a':
        prompt = ''
        prompt_type = ''
    max_chars = 50_000
    length = len(text)
    if not _internal and length > max_chars:
        warnings.warn(
            'Chunking up text into smaller documents so we can add them to '
            'the db.'
        )
        lines = deque(text.splitlines())
        all_res = []
        while lines:
            cur_len = 0
            cur = []
            while cur_len < max_chars and lines:
                line = lines.popleft()
                cur.append(line)
                cur_len += len(line)
            cur_res = store_record(db, user, prompt_type, prompt, tags,
                                   '\n'.join(cur), _internal=True,
                                   doc_id=doc_id)
            all_res += cur_res
        return all_res

    record = {
        'dt': str(datetime.now()),
        'text': text,
        'prompt_type': prompt_type,
        'prompt': prompt,
        'tags': tags,
        'user': user,
        'doc_id': doc_id,
    }
    res = db.put(record)
    return [res]


try:
    DETA_CREDS = load_creds()
except Exception as e:
    warnings.warn('Deta credentials could not be loaded. DETA_CREDS will be '
                  'initialized to an empty dict.\n' + str(e))
    DETA_CREDS = {}
