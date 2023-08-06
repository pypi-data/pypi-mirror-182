import glob
import importlib.util
import sys
from dataclasses import dataclass
from typing import List

from sneks.interface.snek import Snek


@dataclass(frozen=True)
class Submission:
    name: str
    snek: Snek


def get_submissions() -> List[Submission]:
    sneks: List[Submission] = []
    prefix = ".\\submissions\\"
    suffix = "\\submission.py"
    submissions = glob.glob(f"{prefix}*{suffix}")
    for submission in submissions:
        name = submission.removeprefix(prefix).removesuffix(suffix)
        spec = importlib.util.spec_from_file_location(name, submission)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        for i in range(40):
            sneks.append(Submission(f"{name}{i}", module.CustomSnek()))

    return sneks
