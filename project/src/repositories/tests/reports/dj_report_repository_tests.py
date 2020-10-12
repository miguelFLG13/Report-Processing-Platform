from datetime import datetime
from unittest import mock, TestCase

from classes.report import Report
from repositories.reports.dj_report_repository import DjReportRepository


class TestDjReportRepository(TestCase):
    """ Test for Django Report Repository """

    def setUp(self) -> None:
        self.report = Report(
            datetime.now(),
            patient_id="100000",
            document_text="stuff"
        )
        self.report_repository = DjReportRepository()

    @mock.patch('repositories.reports.dj_report_repository.ReportModel')
    def test_add_correct(self, mock_model) -> None:
        """ Test method add in a valid environment """
        mock_model.objects.create.return_value = None
        self.report_repository.add(self.report)
        mock_model.objects.create.assert_called_once()

    @mock.patch('repositories.reports.dj_report_repository.ReportModel')
    def test_add_invalid_report_incorrect(self, mock_model) -> None:
        """ Test method add in a invalid input """
        mock_model.objects.create.return_value = None
        with self.assertRaises(TypeError):
            self.report_repository.add(123)
