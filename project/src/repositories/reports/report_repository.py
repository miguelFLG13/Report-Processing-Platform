from abc import ABC, abstractmethod

from classes.report import Report


class ReportRepository(ABC):
    """ Interface to extend the report repositories """

    @abstractmethod
    def add(self, report: Report) -> None:
        pass
