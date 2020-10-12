from datetime import datetime
from unittest import mock, TestCase

from classes.file import File, PDF_CONTENT_TYPE, TXT_CONTENT_TYPE
from classes.report import Report
from repositories.reports.report_repository import ReportRepository

from use_cases.get_report_information_use_case.services.report_information_processor import ReportInformationProcessor
from use_cases.get_report_information_use_case.get_report_information_use_case import GetReportInformationUseCase


class TestGetReportInformationUseCase(TestCase):
    """ Tests for Get Report Information Use Case """

    def setUp(self) -> None:
        self.correct_output = Report(
            created_at=datetime(2020,10,12,13,0,0),
            patient_id="1000000",
            document_text="stuff"
        )

        self.mock_report_information_processor = mock.create_autospec(ReportInformationProcessor)
        self.mock_report_repository = mock.create_autospec(ReportRepository)

        self.get_report_information_use_case = GetReportInformationUseCase(
            self.mock_report_information_processor,
            self.mock_report_repository
        )

        self.correct_text_file = File(
            title='test.txt',
            content_type=TXT_CONTENT_TYPE,
            content="patient_id=1000000,some_stuff=23|stuff|footer"
        )

    def test_get_report_information_correct(self) -> None:
        """ Test use case using a correct file """
        self.mock_report_information_processor.process.return_value = Report(
            created_at=datetime(2020,10,12,13,0,0),
            patient_id="1000000",
            document_text="stuff"
        )

        report = self.get_report_information_use_case.get(self.correct_text_file)
        self.assertEqual(report, self.correct_output)
        self.mock_report_repository.add.assert_called_once()

    def test_get_report_information_invalid_input_incorrect(self) -> None:
        """ Test use case using a invalid input as a string """
        self.mock_report_information_processor.process.side_effect = TypeError()
        fail_txt = "stuff"

        with self.assertRaises(TypeError):
            self.get_report_information_use_case.get(fail_txt)
        self.mock_report_repository.add.assert_not_called()

    def test_get_report_information_invalid_file_incorrect(self) -> None:
        """ Test use case using a file with a invalid content type """
        self.mock_report_information_processor.process.side_effect = TypeError()

        fail_text_file = File(
            title='test.txt',
            content_type=PDF_CONTENT_TYPE,
            content=b'stuff'
        )

        with self.assertRaises(TypeError):
            self.get_report_information_use_case.get(fail_text_file)
        self.mock_report_repository.add.assert_not_called()
