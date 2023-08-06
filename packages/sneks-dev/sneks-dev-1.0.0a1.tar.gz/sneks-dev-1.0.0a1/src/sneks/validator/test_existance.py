import importlib
import pathlib
import sys

from sneks.core.cell import Cell
from sneks.core.direction import Direction
from sneks.interface.snek import Snek
from sneks.validator import main


def get_module():
    prefix = pathlib.Path(main.path_to_test)
    suffix = "submission.py"
    submissions = list(prefix.glob(f"**/{suffix}"))
    assert 1 == len(submissions)
    submission = submissions[0]
    assert 3 == len(submission.parts)
    name = submission.parts[1]
    spec = importlib.util.spec_from_file_location(name, submission)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module

    return spec, module


def load_module():
    spec, module = get_module()
    spec.loader.exec_module(module)
    return module


def get_custom_snek():
    module = load_module()
    assert issubclass(module.CustomSnek, Snek)
    return module.CustomSnek


def test_import():
    load_module()


def test_class_exists():
    get_custom_snek()


def test_basic_functionality():
    snek = get_custom_snek()()
    snek.food = [Cell(0, 0)]
    snek.body = [Cell(1, 1)]
    assert snek.get_next_direction() in Direction
