from django.conf.urls import include
from django.urls import path


urlpatterns = [
     path('v1/', include('pdf_to_text_api.urls.base_urls')),
]
