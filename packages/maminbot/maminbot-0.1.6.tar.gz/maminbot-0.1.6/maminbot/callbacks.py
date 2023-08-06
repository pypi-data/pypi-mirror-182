from functools import partial
from transformers import TrainerCallback

from maminbot.generation_utils import generate


class TextGenerationCallback(TrainerCallback):
    """Generate 1 or more samples during training to give us a qualitative
    sense of different checkpoints.
    """

    def __init__(self, prompts, path, **generate_kwargs):
        """
        Parameters
        ----------
        prompts: list[str]
        path: str or Path
        generate_kwargs: any
        """
        self.prompts = list(prompts)
        self.path = path
        self.generate_kwargs = generate_kwargs
        self.generate_fn = partial(generate, path=path, **generate_kwargs)
        self.sep = '\n' + '=' * 79 + '\n'
        self.header_fmt = '{sep}GLOBAL STEP {global_step}{sep}'

    def on_evaluate(self, args, state, control, **kwargs):
        with open(self.path, 'a') as f:
            f.write(self.header_fmt.format(sep=self.sep,
                                           global_step=state.global_step))
        for prompt in self.prompts:
            self.generate_fn(kwargs['model'], kwargs['tokenizer'], prompt)