import pytest
import sys


path_to_test = "./submissions/"


def main(test_path: str = None):
    if test_path is not None:
        global path_to_test
        path_to_test = test_path
    sys.exit(pytest.main(["--pyargs", "sneks.validator"]))
