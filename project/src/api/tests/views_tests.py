from rest_framework import status
from rest_framework.test import APITestCase
from tempfile import NamedTemporaryFile
from unittest import mock

from django.urls import reverse


class TestPostPdfToTextAPIView(APITestCase):
    """ Tests POST request to convert Pdf to Text Endpoint """

    def setUp(self) -> None:
        self.url = reverse('pdf_to_text')
        self.correct_output = "stuff"

    def test_pdf_to_text_request_correct(self) -> None:
        """  Test using a regular pdf and the output is the text """
        tmp_file = NamedTemporaryFile(suffix='.pdf')
        tmp_file.write(b'stuff')
        data = {'file': tmp_file}

        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.correct_output)

    def test_pdf_to_text_request_invalid_input_incorrect(self) -> None:
        """  Test using incorrect input """
        data = { 'file': "stuff" }
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_pdf_to_text_request_invalid_file_type_incorrect(self) -> None:
        """  Test using a file without pdf as content type """
        tmp_file = NamedTemporaryFile(suffix='.docx')
        data = {'file': tmp_file}

        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_pdf_to_text_request_empty_input_incorrect(self) -> None:
        """  Test without input """
        response = self.client.post(self.url, data={}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestPostProcessReportAPIView(APITestCase):
    """ Tests POST request to process a report in text Endpoint """

    def setUp(self) -> None:
        self.url = reverse('process_report')
        self.correct_output = {
            'patient_id': 100000,
            'document_text': "stuff"
        }

    def test_process_report_request_correct(self) -> None:
        """  Test using a text file and the output is the report """
        pass

    def test_process_report_request_invalid_input_incorrect(self) -> None:
        """  Test using incorrect input """
        pass

    def test_process_report_request_invalid_file_type_incorrect(self) -> None:
        """  Test using a file without txt as content type """
        pass

    def test_process_report_request_empty_input_incorrect(self) -> None:
        """  Test without input """
        pass
