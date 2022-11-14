from logic.result.i_result import IResult


class RollResultsGenerator(IResult):

    def __init__(self, min_value: int, max_value: int):
        super().__init__(result=None)
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, result, *args, **kwargs):
        self.result = result
        return self

    @property
    def json(self) -> dict:
        return {
            'result': int(self),
            'min value': self.min_value,
            'max value': self.max_value,
        }
