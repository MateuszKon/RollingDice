from abc import ABC, abstractmethod
from typing import Iterator

from logic.randomness.i_random_generator import IRandomGenerator


class IDice(ABC):

    @abstractmethod
    def roll(self) -> int:
        pass

    @abstractmethod
    def rolls(self, n: int) -> Iterator[int]:
        pass


class Dice(IDice):

    def __init__(self, generator: IRandomGenerator, sides: int):
        self.generator = generator
        self.sides = sides

    def roll(self) -> int:
        return self.generator.random_int(self.sides)

    def rolls(self, n: int) -> Iterator[int]:
        i = 0
        while i < n:
            yield self.roll()
            i += 1


if __name__ == "__main__":
    from random import SystemRandom
    from logic.randomness.system_random import RollGenerator
    d10 = Dice(RollGenerator(SystemRandom), 10)
    for roll in d10.rolls(20):
        print(roll)

    # Testing randomness (histogram) of rolling
    # NUMBER_OF_ROLLS = 10000
    #
    # rng = SystemRandom()
    #
    # hist = {i: 0 for i in range(1, 11)}
    # current = hist.get
    # for i in range(NUMBER_OF_ROLLS):
    #     roll = rng.randint(1, 10)
    #     hist[roll] = current(roll, 0) + 1
    #
    # print(hist.values())
    #
    # lists = sorted(hist.items())  # sorted by key, return a list of tuples
    # x, y = zip(*lists)  # unpack a list of pairs into two tuples
    # for x, y in lists:
    #     plt.bar(x, y)
    # plt.axhline(NUMBER_OF_ROLLS / 10)
    # m = np.sum([key * value for key, value in hist.items()]) / NUMBER_OF_ROLLS
    # plt.text(0.6, 0, m)
    # plt.show()