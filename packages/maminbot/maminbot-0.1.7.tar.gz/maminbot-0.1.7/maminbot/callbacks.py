from functools import partial
from pathlib import Path
from transformers import TrainerCallback

from maminbot.generation_utils import generate


class TextGenerationCallback(TrainerCallback):
    """Generate 1 or more samples during training to give us a qualitative
    sense of different checkpoints.
    """

    def __init__(self, prompts, out_dir, **generate_kwargs):
        """
        Parameters
        ----------
        prompts: list[str]
        path: str or Path
        generate_kwargs: any
        """
        self.prompts = list(prompts)
        self.out_dir = out_dir
        self.out_path = Path(out_dir)/'generated_text_samples.txt'
        self.generate_kwargs = generate_kwargs
        self.generate_fn = partial(generate, out_dir=out_dir,
                                   **generate_kwargs)
        self.sep = '\n' + '=' * 79 + '\n'
        self.header_fmt = '{sep}GLOBAL STEP {global_step}{sep}'

    def on_evaluate(self, args, state, control, **kwargs):
        with open(self.out_path, 'a') as f:
            f.write(self.header_fmt.format(sep=self.sep,
                                           global_step=state.global_step))
        for prompt in self.prompts:
            self.generate_fn(kwargs['model'], kwargs['tokenizer'], prompt)