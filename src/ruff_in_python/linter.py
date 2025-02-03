from dataclasses import dataclass
from pathlib import Path
from ruff_in_python.message import Message
from ruff_in_python.parser import parse_file
from ruff_in_python.check import check_ast


@dataclass
class CacheMetadata:
    size: int
    mtime: int


@dataclass
class CheckResult:
    metadata: CacheMetadata
    messages: list[Message]

    def check_path(self, path: Path) -> list[Message]:
        # TODO: skip cache

        # Run the linter
        python_ast = parse_file(path)
        messages = check_ast(path, python_ast)

        # TODO: set cache

        return messages


if __name__ == "__main__":
    result = CheckResult("dummy", [])
    result.check_path("tests/foo.py")

    result = CheckResult("dummy", [])
    result.check_path("tests/bar.py")
