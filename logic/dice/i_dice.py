from abc import ABC, abstractmethod
from typing import Iterator

from logic.result.skill_roll_result_generator import IResult


class IDice(ABC):

    def __init__(self, sides: int, *args, **kwargs):
        self.sides = sides

    @abstractmethod
    def roll(self) -> IResult:
        pass

    @abstractmethod
    def rolls(self, n: int) -> Iterator[IResult]:
        pass
