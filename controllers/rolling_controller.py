from abc import ABC, abstractmethod
from typing import Union

from dice.result.result import Result
from dice.skill_roll import ExtraDiceType


class IRollingController(ABC):

    @abstractmethod
    def roll_skill_test(
            self,
            extra_dices_number: int = 0,
            extra_dices_type: Union[ExtraDiceType, None] = None
    ) -> Result:
        """
        Make test roll (d100) with optionally some extra dices
        :param extra_dices_number: number of extra dices rolled
        must be natural number, if different that 0, then next param
        must be also defined
        :param extra_dices_type: only considered if previous param is
        not equal to 0
        :return: result of test
        """
        pass

    @abstractmethod
    def roll_custom(self):
        pass


class RollingController(IRollingController):

    pass
