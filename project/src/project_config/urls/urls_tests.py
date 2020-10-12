from django.conf.urls import include
from django.urls import path


urlpatterns = [
     path('v1/', include('project_config.urls.base_urls')),
]
