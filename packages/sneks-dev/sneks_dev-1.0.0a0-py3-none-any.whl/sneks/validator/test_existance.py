import glob
import importlib
import sys

from sneks.core.cell import Cell
from sneks.core.direction import Direction


def test_import():
    prefix = ".\\submissions\\"
    suffix = "\\submission.py"
    submissions = glob.glob(f"{prefix}*{suffix}")
    for submission in submissions:
        name = submission.removeprefix(prefix).removesuffix(suffix)
        spec = importlib.util.spec_from_file_location(name, submission)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)


def test_class_exists():
    from sneks.interface.snek import Snek
    from sneks.template.submission import CustomSnek

    assert issubclass(CustomSnek, Snek)


def test_basic_functionality():
    from sneks.template.submission import CustomSnek

    snek = CustomSnek()
    snek.food = [Cell(0, 0)]
    snek.body = [Cell(1, 1)]
    assert snek.get_next_direction() in Direction
