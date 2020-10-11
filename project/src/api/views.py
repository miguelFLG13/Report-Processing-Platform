from pypendency.builder import container_builder
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.exceptions import SuspiciousOperation

from classes.file import File

from api.services import is_pdf_file


class PdfToTextAPIView(APIView):
    """
    POST Request to manage the conversion to text of a pdf
    """
    permission_classes = ()

    def dispatch(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            raise SuspiciousOperation("Incorrect Input Payload")

        if not is_pdf_file(file):
            raise SuspiciousOperation("Incorrect File Type")

        return super().dispatch(request, *args, **kwargs)

    def post(self, request: Request):
        use_case = container_builder.get(
            "use_cases.extract_pdf_text_use_case.extract_pdf_text_use_case.ExtractPdfTextUseCase"
        )

        pdf = request.FILES['file'].open('r')
        pdf_file = File(
            title=pdf.name,
            content_type=pdf.content_type,
            content=pdf.read()
        )

        text = use_case.extract(pdf_file)
        return Response(
            text,
            status=status.HTTP_200_OK
        )
