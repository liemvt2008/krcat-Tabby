import typing

from langdetect.lang_detect_exception import LangDetectException
from langdetect.language import Language

from kde.engines.base import BaseEngine
from kde.engines.models import EngineResult, UNKNOWN_VALUE_STR


class LangDetectEngine(BaseEngine):
    MIN_TEXT_LENGTH = 14
    MIN_WORDS_COUNT = 4
    UNKNOWN = UNKNOWN_VALUE_STR
    EMPTY_STRING = ''

    def load_model(self):
        import langdetect
        langdetect.DetectorFactory.seed = 0
        return langdetect

    def preprocess(self, input_: typing.Any) -> typing.Any:
        if not input_:
            return self.EMPTY_STRING
        return input_.strip()

    def _process(self, input_: typing.Any) -> typing.List[Language]:
        try:
            return self.model.detect_langs(input_)
        except LangDetectException:
            return [Language(self.UNKNOWN, self.UNKNOWN_PROBABILITY)]

    def postprocess(self, result: typing.List[Language]) -> EngineResult:
        language = result[0].lang.strip().lower().split('-')[0]
        if language is None:
            return self.make_unknown_result()

        return EngineResult(
            value=language, probability=result[0].prob, engine_name=self.__class__.__name__
        )

    def _is_short_text(self, text: str) -> bool:
        return not text or len(text) < self.MIN_TEXT_LENGTH or \
               len(text.split()) < self.MIN_WORDS_COUNT
