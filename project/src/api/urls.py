from django.urls import path

from api.views import PdfToTextAPIView, ProcessReportAPIView


urlpatterns = [
    path('pdf-to-text/', PdfToTextAPIView.as_view(), name='pdf_to_text'),
    path('process-report/', ProcessReportAPIView.as_view(), name='process_report'),
]
