import ast
from ruff_in_python.parser import parse


def test_parser():
    stmt = "print(123)"
    res = parse(stmt)
    assert isinstance(res, ast.Module)
