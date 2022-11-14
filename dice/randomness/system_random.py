from random import Random

from dice.randomness.i_random_generator import IRandomGenerator


class RollGenerator(IRandomGenerator):

    def __init__(self, generator_type: type(Random), *args, **kwargs):
        self.generator: Random = generator_type(*args, **kwargs)

    def random_int(self, max_int: int, min_int: int = 1) -> int:
        return self.generator.randint(min_int, max_int)


if __name__ == "__main__":
    from random import SystemRandom

    generator = RollGenerator(SystemRandom)
    print(generator.random_int(10))



