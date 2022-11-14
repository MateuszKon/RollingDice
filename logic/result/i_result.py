from abc import ABC, abstractmethod


class IResult(ABC):

    def __init__(self, result: int, *args, **kwargs):
        self.result = result

    def __int__(self) -> int:
        return self.result

    def __str__(self) -> str:
        return str(self.result)

    @property
    @abstractmethod
    def json(self) -> dict:
        """
        Returns dictionary with all information about result
        """
        pass
