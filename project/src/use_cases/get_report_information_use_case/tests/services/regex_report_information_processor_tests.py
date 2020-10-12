from datetime import datetime
from unittest import mock, TestCase

from classes.file import File, PDF_CONTENT_TYPE, TXT_CONTENT_TYPE
from classes.report import Report
from classes.structure import Structure
from repositories.reports.structure_repository import StructureRepository

from use_cases.get_report_information_use_case.services.regex_report_information_processor import RegexReportInformationProcessor


class TestRegexReportInformationProcessor(TestCase):
    """ Tests for Regex Report Information Processor service """

    def setUp(self) -> None:
        self.correct_output = Report(
            created_at=datetime(2020,10,12,13,0,0),
            patient_id="1000000",
            document_text="stuff"
        )

        self.correct_text_file =  File(
            title='test.txt',
            content_type=TXT_CONTENT_TYPE,
            content="patient_id=1000000,some_stuff=23|stuff|footer"
        )

        self.structure_repository = mock.create_autospec(StructureRepository)
        self.structure = mock.MagicMock(spec=Structure)
        self.structure.main_separator = "|"
        self.structure.header_separator = ","
        self.structure.header_key_separator = "="

    @mock.patch('use_cases.get_report_information_use_case.services.regex_report_information_processor.re')
    def test_process_report_information_correct(self, mock_re) -> None:
        """ Test the service with a valid file """
        mock_re.split.side_effect = [
            ["patient_id=1000000,some_stuff=23", "stuff", "footer"],
            ["patient_id=1000000"],
            ["patient_id", "1000000"],
            ["some_stuff=23"],
            ["some_stuff", "23"]
        ]
        self.structure_repository.get_all.return_value = [self.structure]
        regex_report_information_processor = RegexReportInformationProcessor(
            self.structure_repository
        )

        report = regex_report_information_processor.process(self.correct_text_file)

        self.assertEqual(report, self.correct_output)

    def test_process_report_information_invalid_input_incorrect(self) -> None:
        """ Test the service with a invalid input file """
        fail_txt = "stuff"

        self.structure_repository.get_all.return_value = []
        regex_report_information_processor = RegexReportInformationProcessor(
            self.structure_repository
        )

        with self.assertRaises(TypeError):
            regex_report_information_processor.process(fail_txt)

    def test_process_report_information_invalid_file_incorrect(self) -> None:
        """ Test the service with a file with a invalid content type """
        fail_text_file = File(
            title='test.txt',
            content_type=PDF_CONTENT_TYPE,
            content=b'stuff'
        )

        self.structure_repository.get_all.return_value = []
        regex_report_information_processor = RegexReportInformationProcessor(
            self.structure_repository
        )

        with self.assertRaises(TypeError):
            regex_report_information_processor.process(fail_text_file)


    def test_process_report_information_without_structures_incorrect(self) -> None:
        """ Test the service without structures """
        self.structure_repository.get_all.return_value = []
        regex_report_information_processor = RegexReportInformationProcessor(
            self.structure_repository
        )

        with self.assertRaises(Exception):
            regex_report_information_processor.process(self.correct_text_file)
