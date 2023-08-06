from itertools import cycle
import numpy as np
import torch
from torch.utils.data import Dataset
from tqdm.auto import tqdm
import warnings

from maminbot.db_utils import fetch_records
from maminbot.utils import dataclass_to_dict


class LanguageModelDataset(Dataset):

    def __init__(self, tokenizer, texts=None, x=None,
                 fixed_len=True, drop_last=False, **config):
        """
        Parameters
        ----------
        tokenizer
        texts: List[str] or None
            List of pieces of text. Provide either this OR `texts`.
        x: List[dict] or None
            List of dicts, each containing at least an "input_ids" key.
            This is the result of one of our chunkify methods.
            Provide either this OR `texts`. Useful for creating subsets or
            train/test splits.
        fixed_len: bool
            If True, make all token sequences the same length (model max
            length). This lets us avoid using padding and can dramatically
            speed up training.
        drop_last: bool
            Only used when fixed_len=True. Drops the last sequence if it's too
            short because otherwise the sequences wouldn't all be the
            same length.
        config: any
            Specified automatically when using from_data_args method, which is
            used in s00 to train a model from the command line. It's just a
            dict containing all the DataTrainingArguments provided by the user.
        """
        if tokenizer.eos_token_id is None:
            raise ValueError('Tokenizer eos_token_id cannot be None.')

        self.tokenizer = tokenizer
        config.update(fixed_len=fixed_len, drop_last=drop_last)
        # x will be a list of dicts. Input validation must remain after the two
        # lines above (or pass in tokenizer and other inputs too).
        self._validate_inputs(x, texts, config)
        self.x = x or self.chunkify(texts, fixed_len=fixed_len,
                                    drop_last=drop_last)
        self.config = config

    def _validate_inputs(self, x, texts, config):
        """Because this class allows passing in either raw text (list[str]) or
        pre-defined dataset items (dict containing tensor(s)) AND we support
        a couple different modes (dataset items may or may not contain
        attention masks, depending on choice of fixed_len in init), we need to
        do a lot of validation of input args.

        Parameters
        ----------
        x: list[dict] or None
        texts: list[str] or None
        config: dict
        """
        if not x:
            # Can skip most validation because we'll be constructing the inputs
            # ourselves.
            assert texts, 'Texts must be provided when x is null.'
            return

        if texts:
            warnings.warn('Texts will be ignored because x is not None.')
        first = list(x[0])
        if config['fixed_len']:
            # Last item may be different length when drop_last is True, so we
            # discard it in that case (only for validation purposes - we're
            # just changing the local variable here).
            x = x[:len(x) - config['drop_last']]
            lengths = set(len(row['input_ids']) for row in x)
            assert len(lengths) == 1, 'Found mismatched lengths when ' \
                                      'fixed_len=True.'
            assert next(iter(lengths)) == self.tokenizer.model_max_length, \
                'Sequence length should equal model max length when ' \
                'fixed_len=True.'
            expected_first = ['input_ids']
            assert first == expected_first, \
                f'Each dataset item should only have keys {expected_first} ' \
                f'when fixed_len=True, but found: {first}'
        else:
            expected_first = ['attention_mask', 'input_ids']
            first = sorted(first)
            assert first == ['attention_mask', 'input_ids'], \
                f'Each dataset item should have keys {expected_first} ' \
                f'when fixed_len=False. Instead found {first}.'

    def chunkify(self, texts, fixed_len, drop_last):
        """Chunk up texts into dataset items (dicts of tensor(s)).

        Parameters
        ----------
        texts: list[str]
        fixed_len: bool
        drop_last: bool

        Returns
        -------
        list[dict]
        """
        if fixed_len:
            chunks = self._chunkify_fixed_len(texts, drop_last=drop_last)
        else:
            chunks = self._chunkify_variable_length(texts)
        return list(chunks)

    def _chunkify_variable_length(self, texts):
        # This method chunks up each row separately such that each chunk
        # contains only 1 source sentence.
        warnings.warn('We recommend setting fixed_len=True to speed up '
                      'training. This implementation is far slower.')

        # Fewer dot accesses in loop speeds things up when dataset is huge.
        tokenizer = self.tokenizer
        chunk_size = tokenizer.model_max_length
        for row in tqdm(texts, desc='Tokenizing corpus...'):
            tokens = tokenizer(row, return_tensors='pt')
            chunks = [{'input_ids': chunk.squeeze(0),
                       'attention_mask': torch.ones(chunk.shape[-1])}
                      for chunk
                      in tokens['input_ids'].split(chunk_size, dim=-1)]
            yield from chunks

    def _chunkify_fixed_len(self, texts, drop_last=True):
        # Chunks dataset up into fixed length chunks so we don't require
        # padding or masking during training.
        # Fewer dot accesses in loop speeds things up when dataset is huge.
        tokenizer = self.tokenizer
        chunksize = tokenizer.model_max_length
        if not isinstance(texts, list):
            texts = list(texts)
        flat = []
        for row in tqdm(texts):
            flat.extend(
                tokenizer(row, truncation=False, padding=False).input_ids
                + [tokenizer.eos_token_id]
            )
        total_tokens = len(flat)
        for i in range(0, total_tokens, chunksize):
            chunk = flat[i:i + chunksize]
            # When we train on a tiny subset, we could end up with less than 1
            # full max len sequence, so we make sure we never drop the first
            # chunk or we could end up with a ds of length 0.
            cur_length = len(chunk)
            if cur_length < chunksize and i > 0 and drop_last:
                warnings.warn(f'Dropping last chunk with length {len(chunk)}:'
                              f'\n\n{tokenizer.decode(chunk)}')
                break
            # If our first sequence is shorter than the max, we don't need to
            # pad it because all our sequences will be the same length
            # regardless. That should really only happen when testing on tiny
            # toy datasets.
            if i > 0:
                chunk = pad_with_self(chunk, chunksize, tokenizer.eos_token_id)
            yield {'input_ids': torch.tensor(chunk, dtype=torch.long)}

    @classmethod
    def from_data_args(cls, tokenizer, data_args):
        """Create dataset from DataArguments in s00 (i.e. when we train a model
        from the command line).

        Parameters
        ----------
        tokenizer
        data_args: Union[dict, DataTrainingArguments]
        """
        kwargs = dataclass_to_dict(data_args)
        df = fetch_records(**kwargs)
        ds = cls(tokenizer, texts=df.text.tolist(), **kwargs)
        if kwargs.get('fast_dev_run'):
            # One training batch, one validation batch.
            n_seq = kwargs.get('batch_size', 1) * 2
            ds = ds.subset(n_seq)
        return ds

    def train_test_split(self, test_size, seed=0):
        """
        Parameters
        ----------
        test_size: int or float
            If float, should be in [0, 1). If int, should be in [0, len(self)).
        seed: int

        Returns
        -------
        dict[str, LanguageModelDataset]: Key 'train' is always present. Key
        'test' is only present if test_size > 0.
        """
        if not test_size:
            return {'train': self}
        length = len(self)
        if isinstance(test_size, float):
            test_size = int(test_size * length)
        if test_size >= length:
            raise ValueError(
                'Your requested test set size is too big. You only have '
                f'{length} sequences available for training and testing '
                f'combined.'
            )
        test_idx = set(
            np.random.RandomState(seed).choice(
                length, test_size, replace=False
            )
        )
        train_x = []
        test_x = []
        for i, row in enumerate(self.x):
            if i in test_idx:
                test_x.append(row)
            else:
                train_x.append(row)
        cls = type(self)
        ds_train = cls(self.tokenizer, x=train_x, **self.config)
        ds_test = cls(self.tokenizer, x=test_x, **self.config)
        return {'train': ds_train,
                'test': ds_test}

    def subset(self, n_sequences=1, strict=False):
        """Create a subset of an existing LanguageModelDataset.

        Parameters
        ----------
        n_sequences
        strict

        Returns
        -------
        LanguageModelDataset
        """
        if n_sequences > len(self):
            msg = (f'Cannot create a subset with {n_sequences} '
                   f'sequences when the original datset only has '
                   f'{len(self)}.')
            if strict:
                raise ValueError(msg)
            else:
                warnings.warn(msg)
        cls = type(self)
        return cls(self.tokenizer, x=self.x[:n_sequences], **self.config)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, i):
        return self.x[i]


def cycle_chunks(arr, chunksize, sep):
    """Like itertools.cycle but we yield k items at a time instead of 1
    and we insert a separator item between the last and first item in the
    sequence when we loop around. Used to pad out a batch of text when training
    with fixed sequence lengths (hate to throw away data when it's scarce).

    Parameters
    ----------
    arr: list
    chunksize: int
        Desired size of each chunk. The sep char counts as 1, the same as each
        item in the original list.
    sep: any
        Typically the same type as the items in arr.

    Returns
    -------
    list

    Examples
    --------
    ```
    chunksize = 7
    for i, row in enumerate(iter_chunks([0, 1, 2, 3, 4], chunksize, '<EOS>')):
        print(row)
        assert len(row) == chunksize
        # Exit at arbitrary point to prevent infinite loop.
        if i >= 10: break
    ```

    [0, 1, 2, 3, 4, '<EOS>', 0]
    [1, 2, 3, 4, '<EOS>', 0, 1]
    [2, 3, 4, '<EOS>', 0, 1, 2]
    [3, 4, '<EOS>', 0, 1, 2, 3]
    [4, '<EOS>', 0, 1, 2, 3, 4]
    ['<EOS>', 0, 1, 2, 3, 4, '<EOS>']
    [0, 1, 2, 3, 4, '<EOS>', 0]
    [1, 2, 3, 4, '<EOS>', 0, 1]
    [2, 3, 4, '<EOS>', 0, 1, 2]
    [3, 4, '<EOS>', 0, 1, 2, 3]
    [4, '<EOS>', 0, 1, 2, 3, 4]
    """
    arr = list(arr) + [sep]
    generator = cycle(arr)
    while True:
        chunk = []
        for i, x in enumerate(generator, 1):
            chunk.append(x)
            if i == chunksize: break
            i += 1
        yield chunk


def pad_with_self(arr, size, sep):
    """Pad out a sequence to a desired size by looping around on itself.
    See cycle_chunks in the same module - this just takes the first one.

    Parameters
    ----------
    arr: list
        Typically a list of ints (token IDs).
    size: int
        Desired size.
    sep: any
        Usually an int. Should typically be the same type as the items in arr.

    Returns
    -------
    list: Has same input type as the items in arr (assuming sep has same type).
    If arr is already the desired size, we return itself. If it's longer than
    the desired size, we return arr[:size].
    """
    res = next(cycle_chunks(arr, size, sep))
    assert len(res) == size, f'Expected len={size} but got len={len(res)}.'
    return res
