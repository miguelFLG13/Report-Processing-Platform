from unittest import mock

from django.test import TestCase

from classes.file import File

from use_cases.extract_pdf_text_use_case.extract_pdf_text_use_case import ExtractPdfTextUseCase
from use_cases.extract_pdf_text_use_case.services.pdf_to_text_file_converter import PdfToTextFileConverter
from use_cases.extract_pdf_text_use_case.conf import PDF_CONTENT_TYPE, TXT_CONTENT_TYPE


class TestExtractPdfTextUseCase(TestCase):
    """ Tests for Extract Pdf Text Use Case """

    def setUp(self) -> None:
        self.correct_output = "stuff"
        self.mock_pdf_to_text_file_converter = mock.create_autospec(PdfToTextFileConverter)
        self.extract_pdf_text_use_case = ExtractPdfTextUseCase(self.mock_pdf_to_text_file_converter)

    def test_convert_pdf_to_text_correct(self) -> None:
        """ Test extractor using a regural pdf File and getting the text """
        self.mock_pdf_to_text_file_converter.convert.return_value = File(
            title='test.pdf',
            content_type=TXT_CONTENT_TYPE,
            content='stuff'
        )

        pdf_file = File(
            title='test.pdf',
            content_type=PDF_CONTENT_TYPE,
            content='stuff'
        )

        output_text = self.extract_pdf_text_use_case.extract(pdf_file)
        self.assertEqual(output_text, self.correct_output)

    def test_convert_pdf_to_text_invalid_type_incorrect(self) -> None:
        """ Test extractor using a invalid input """
        self.mock_pdf_to_text_file_converter.convert.side_effect = TypeError()
        fail_pdf = "stuff"
        with self.assertRaises(TypeError):
            self.extract_pdf_text_use_case.extract(fail_pdf)

    def test_convert_pdf_to_text_invalid_file_incorrect(self) -> None:
        """ Test extractor using a file with a invalid content type """
        self.mock_pdf_to_text_file_converter.convert.side_effect = TypeError()
        fail_pdf = File(
            title='test.pdf',
            content_type=TXT_CONTENT_TYPE,
            content='stuff'
        )

        with self.assertRaises(TypeError):
            self.extract_pdf_text_use_case.extract(fail_pdf)
