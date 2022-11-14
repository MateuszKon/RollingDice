from abc import ABC, abstractmethod
from typing import Type


class Result:

    def __init__(self, result: int, *args, **kwargs):
        self.result = result
        self.args = args
        self.kwargs = kwargs

    def __int__(self) -> int:
        return self.result

    def __str__(self) -> str:
        return str(self.result)

    @property
    def json(self) -> dict:
        """
        Returns dictionary with all information about result
        """
        j = {}
        j.update(self.kwargs)
        j['result'] = self.result
        return j


class ResultFactory:

    def __init__(self, result_cls: Type[Result], *args, **kwargs):
        self.result_cls = result_cls
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        d = self.kwargs
        d.update(kwargs)
        return self.result_cls(
            *args,
            *self.args,
            **d
        )


if __name__ == "__main__":
    r = Result(10, label='123')
    print(r.json)
    print(r)

    factory = ResultFactory(Result, abe="adsdas")
    r = factory(7, dada="dada")
    print(r.json)
