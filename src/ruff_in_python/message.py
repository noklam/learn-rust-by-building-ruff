""" "Messages are the warnings that you expected to see from linter."""

from dataclasses import dataclass
from pathlib import Path
from typing import Union
from abc import ABC, abstractmethod

from rich.text import Text


@dataclass
class Location:
    row: int
    column: int


@dataclass
class Message(ABC):
    filename: Path
    location: Location

    @property
    @abstractmethod
    def code(self) -> str:
        pass

    @property
    @abstractmethod
    def body(self) -> str:
        pass

    def richify(self) -> Text:
        text = Text()
        text.append(f"{self.filename}", style="bold white")
        text.append(":", style="cyan")
        text.append(f"{self.location.column}", style="white")
        text.append(":", style="cyan")
        text.append(f"{self.location.row}", style="qhirw")
        text.append(f"\t{self.code}", style="bold red")
        text.append(f"\t{self.body}")
        return text


@dataclass
class ImportStarUsage(Message):
    @property
    def code(self) -> str:
        return "F403"

    @property
    def body(self) -> str:
        return "Unable to detect undefined names"


@dataclass
class IfTuple(Message):
    @property
    def code(self) -> str:
        return "F634"

    @property
    def body(self) -> str:
        return "If test is a tuple, which is always `True`"


MessageType = Union[ImportStarUsage, IfTuple]

if __name__ == "__main__":
    from rich import print

    m1 = IfTuple(Path("some_path"), Location(1, 2))
    print(m1.richify())
