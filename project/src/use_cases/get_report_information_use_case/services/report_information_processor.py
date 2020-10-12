from abc import ABC, abstractmethod

from classes.report import Report


class ReportInformationProcessor(ABC):
    """ Interface to extend the processors by method to get the info """

    @abstractmethod
    def process(self, text: str) -> Report:
        pass
