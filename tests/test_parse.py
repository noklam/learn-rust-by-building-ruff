import ast
from ruff_in_python.parser import parse_file


def test_parser():
    stmt = "tests/foo.py"
    res = parse_file(stmt)
    assert isinstance(res, ast.Module)
