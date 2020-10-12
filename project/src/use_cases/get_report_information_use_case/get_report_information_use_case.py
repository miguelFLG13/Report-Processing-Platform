from classes.file import File
from classes.report import Report
from repositories.reports.report_repository import ReportRepository

from use_cases.get_report_information_use_case.services.report_information_processor import ReportInformationProcessor


class GetReportInformationUseCase:
    """ Use Case to complete the report information in a text file """

    def __init__(
        self,
        report_information_processor: ReportInformationProcessor,
        report_repository: ReportRepository
    ) -> None:
        self.__report_information_processor = report_information_processor
        self.__report_repository = report_repository

    def get(self, text_file: File) -> Report:
        report = self.__report_information_processor.process(text_file)
        self.__report_repository.add(report)
        return report
