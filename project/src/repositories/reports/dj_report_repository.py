from dataclasses import asdict

from apps.reports.models import ReportModel
from classes.report import Report

from repositories.reports.report_repository import ReportRepository


class DjReportRepository(ReportRepository):
    """ Repository to manage the Report with Django ORM """

    def add(self, report: Report) -> None:
        ReportModel.objects.create(**asdict(report))
