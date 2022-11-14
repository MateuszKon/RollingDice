from abc import ABC, abstractmethod
from typing import Iterator

from dice.result.result import Result


class IDice(ABC):

    @abstractmethod
    def roll(self) -> Result:
        pass

    @abstractmethod
    def rolls(self, n: int) -> Iterator[Result]:
        pass
