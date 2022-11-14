from abc import ABC, abstractmethod


class IRandomGenerator(ABC):

    @abstractmethod
    def random_int(self, max_int: int, min_int: int = 1) -> int:
        pass
