import re
import typing

from kde.engines.base import BaseEngine
from kde.engines.models import EngineResult, UNKNOWN_VALUE_STR


class RegexEngine(BaseEngine):
    EMPTY_STRING = ''
    UNKNOWN = [UNKNOWN_VALUE_STR]

    def load_model(self):
        return re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')

    def preprocess(self, input_: str) -> str:
        if not input_:
            return self.EMPTY_STRING
        return input_.strip()

    def _process(self, input_: typing.Any) -> typing.List[str]:
        emails = self.model.findall(input_)
        if emails:
            return [email.lower() for email in emails]

    def postprocess(self, result: typing.List[str]) -> EngineResult:
        if not result:
            return self.make_unknown_result()

        return EngineResult(value=list(set(result)), engine_name=self.__class__.__name__)
