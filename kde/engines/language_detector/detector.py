import re
import typing
from functools import cached_property

from kde.engines.models import EngineResult


class LanguageDetector:
    SENTENCE_SPLITTER = re.compile(r'[\!\?\.\n\t]')

    @cached_property
    def lang_detect_engine(self):
        from .langdetect_engine import LangDetectEngine
        return LangDetectEngine()

    def detect_language(self, paragraph: str) -> typing.List[EngineResult]:
        if not (paragraph and paragraph.strip()):
            return [self.lang_detect_engine.make_unknown_result()]

        sentence_languages = []
        for sentence in re.split(self.SENTENCE_SPLITTER, paragraph.strip()):
            sentence = sentence.strip()
            if sentence:
                result = self.lang_detect_engine.process(sentence)
                result.properties = {'sentence': sentence}
                sentence_languages.append(result)
        return sentence_languages
