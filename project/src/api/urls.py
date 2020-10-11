from django.urls import path

from api.views import PdfToTextAPIView


urlpatterns = [
    path('pdf-to-text/', PdfToTextAPIView.as_view(), name='pdf_to_text'),
]
