from django.test import TestCase

from classes.file import File

from use_cases.extract_pdf_text_use_case.services.pdf_to_text_file_converter import PdfToTextFileConverter
from use_cases.extract_pdf_text_use_case.conf import PDF_CONTENT_TYPE, TXT_CONTENT_TYPE


class TestPdfToTextFileConverter(TestCase):
    """ Tests for Pdf To Text File Converter """

    def setUp(self) -> None:
        self.correct_output = File(
            title="test.pdf.txt",
            content_type=TXT_CONTENT_TYPE,
            content="stuff"
        )

        self.pdf_to_text_file_converter = PdfToTextFileConverter()

    def test_convert_pdf_to_text_correct(self) -> None:
        """ Test converter using a regural pdf File and getting a Text File """
        pdf_file = File(
            title='test.pdf',
            content_type=PDF_CONTENT_TYPE,
            content=b'stuff'
        )

        output_file = self.pdf_to_text_file_converter.convert(pdf_file)
        self.assertEqual(output_file, self.correct_output)

    def test_convert_pdf_to_text_invalid_file_incorrect(self) -> None:
        """ Test converter using a file with a invalid content type """
        fail_pdf = File(
            title='test.pdf',
            content_type=TXT_CONTENT_TYPE,
            content=b'stuff'
        )

        with self.assertRaises(TypeError):
            self.pdf_to_text_file_converter.convert(fail_pdf)

    def test_convert_pdf_to_text_invalid_type_incorrect(self) -> None:
        """ Test converter using a invalid input """
        fail_pdf = "stuff"
        with self.assertRaises(TypeError):
            self.pdf_to_text_file_converter.convert(fail_pdf)
