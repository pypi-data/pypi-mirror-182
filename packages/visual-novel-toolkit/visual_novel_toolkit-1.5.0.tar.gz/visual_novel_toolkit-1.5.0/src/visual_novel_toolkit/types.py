from typing import Protocol
from typing import TypedDict


class YASpeller(TypedDict, total=False):
    dictionary: list[str]


class Words(Protocol):
    def get(self) -> list[str]:
        raise RuntimeError

    def set(self, value: list[str]) -> None:
        raise RuntimeError
