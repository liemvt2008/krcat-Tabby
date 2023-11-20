from functools import cached_property
from logging import getLogger


class TextEnricher:

    def __init__(self):
        self._logger = getLogger(self.__class__.__name__)

    @cached_property
    def email_extractor(self):
        from kde.engines.email_extractor import EmailExtractor
        return EmailExtractor()

    @cached_property
    def language_detector(self):
        from kde.engines.language_detector import LanguageDetector
        return LanguageDetector()

    def extract_email(self, input_text):
        result = self.email_extractor.extract_emails(input_text)
        self._logger.info(f'Extracted {result} from input {input_text}')
        return result.to_dict()

    def detect_language(self, input_text):
        results = self.language_detector.detect_language(input_text)
        self._logger.info(f'Detected languages {results} from input {input_text}')
        return [result.to_dict() for result in results]
