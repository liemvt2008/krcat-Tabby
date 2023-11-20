import typing
from functools import cached_property

from .models import EngineResult


class BaseEngine:
    ENGINE_NAME = ''
    UNKNOWN = None
    UNKNOWN_PROBABILITY = 1.0

    @cached_property
    def model(self):
        return self.load_model()

    def load_model(self):
        """
        :return:
        """

    def make_unknown_result(self, engine_name: str = None) -> EngineResult:
        return EngineResult(
            value=self.UNKNOWN, probability=self.UNKNOWN_PROBABILITY,
            engine_name=engine_name or self.__class__.__name__)

    def postprocess(self, result: typing.Any) -> EngineResult:
        raise NotImplementedError

    def preprocess(self, input_: typing.Any) -> typing.Any:
        return input_

    def process(self, input_: typing.Any) -> EngineResult:
        processed_input = self.preprocess(input_)
        result = self._process(processed_input)
        return self.postprocess(result)

    def _process(self, input_: typing.Any) -> EngineResult:
        raise NotImplementedError
