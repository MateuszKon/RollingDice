from abc import ABC, abstractmethod
from enum import Enum
from typing import Union

from logic.result.skill_roll_result_generator import IResult


class ExtraDiceType(Enum):
    BONUS = 1
    PENALTY = 2


class IRolling(ABC):

    @abstractmethod
    def roll_test(
            self,
            extra_dices_number: int = 0,
            extra_dices_type: Union[ExtraDiceType, None] = None
    ) -> IResult:
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
