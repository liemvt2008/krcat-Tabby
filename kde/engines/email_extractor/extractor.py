from functools import cached_property

from kde.engines.models import EngineResult


class EmailExtractor:

    @cached_property
    def regex_engine(self):
        from .regex_engine import RegexEngine
        return RegexEngine()

    def extract_emails(self, paragraph: str) -> EngineResult:
        if not paragraph:
            return self.regex_engine.make_unknown_result()

        return self.regex_engine.process(paragraph)
