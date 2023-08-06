from datetime import datetime
from pathlib import Path
import sys

from htools.core import flatten
from maminbot import config as cfg


def load_hf_api_key(paths=('~/.huggingface', '~/secrets/.huggingface')):
    """
    Parameters
    ----------
    paths: Iterable[str]
        The paths to check for huggingface api keys. Order matters: we return
        the contents of the first non-empty file in the list.

    Returns
    -------
    str: Huggingface api key. Guaranteed to be truthy if we hit the return
    statement. Raises a FileNotFoundError if NONE of the paths exist/contain
    truthy strings.
    """
    for path in paths:
        try:
            with open(Path(path).expanduser(), 'r') as f:
                key = f.read().strip()
        except FileNotFoundError:
            key = ''
        if key: return key
    raise FileNotFoundError('Could not find any huggingface api key. '
                            f'Checked paths: {paths}')


def update_cli_command(**kwargs):
    """Used in s01 to add default args to our language model training script.
    This is helpful because adding defaults in dataclass subclasses is
    surprisingly difficult. If the user actually did specify the field, the
    defaults are not applied.

    Warning: this assumes a command like 'python train.py --user adrienne',
    or `python train.py --user=adrienne'. It is not built to handle boolean
    flags like 'python train.py --do_eval', though
    'python train.py --do_eval True' would work..

    Parameters
    ----------
    kwargs: any
    """
    sys.argv = flatten([arg.split('=') if '=' in arg else arg
                        for arg in sys.argv])
    for k, v in kwargs.items():
        if f'--{k}' not in sys.argv:
            sys.argv.extend([f'--{k}', str(v)])


def get_cli_value(field):
    """Extract the value entered at the command line by searching sys.argv.
    I.e. if user enters 'python train.py --lr .003' and the script calls
    get_cli_value('lr'), we would get .003 (as a str). If the desired field
    was not provided, we raise a ValueError.

    Parameters
    ----------
    field: str

    Returns
    -------
    str
    """
    for cur, next in zip(sys.argv, sys.argv[1:]):
        if cur == '--' + field:
            return next
    raise ValueError(f'Field {field!r} not found.')


def datetime_dirname(subdir='data/models', as_path=True, mkdir=False):
    """Return path to a new directory named like
    "~/maminbot/data/models/2022.12.31__19:49:37". In this case,
    subdir='data/models' (the default) and the date would be December 31, 2022
    and the time would be 7:49:37 pm.

    Parameters
    ----------
    subdir: str or Path
        Relative to maminbot project root.
    as_path: bool
        If True, we return a pathlib.Path obj. Str otherwise.

    Returns
    -------
    str or Path: depends on value of as_path param.
    """
    dt = datetime.now().strftime("%Y.%m.%d__%H.%M.%S")
    path = cfg.root/f'{subdir}/{dt}'
    if mkdir:
        path.mkdir()
    if not as_path:
        path = str(path)
    return path


def model_output_dirname():
    """Wrapper to get a model output dirname for s00.

    Returns
    -------
    str: Something like
    '~/maminbot/data/models/harrison/mlm/2022.12.31__18.33.19'.
    """
    user = get_cli_value("user")
    try:
        mlm = get_cli_value("mlm")
    except ValueError:
        mlm = False
    return datetime_dirname(
        f'data/models/{user}/{"mlm" if mlm else "clm"}',
        as_path=False
    )


def dataclass_to_dict(obj):
    """For cases where a dataclass or dict may be provided. This always returns
    a dict. If a dict is passed in, we make a copy to avoid mutating the
    input later.

    Parameters
    ----------
    obj: Dataclass or dict
    """
    if not isinstance(obj, dict):
        obj = getattr(obj, '__dict__', {})
    else:
        # Create a new object to avoid mutating the input.
        obj = dict(obj)
    return obj
