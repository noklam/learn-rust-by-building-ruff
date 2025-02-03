import ast
from pathlib import Path


def pretty_print_ast(self):
    # Monkeypatch so it's easier to visualise the ast module
    return ast.dump(self, indent=2)


ast.Module.__repr__ = pretty_print_ast


def parse_file(path: Path):
    with open(path) as f:
        res = ast.parse(f.read())
        return res.body
