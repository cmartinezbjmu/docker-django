from django.conf.urls import url
from .views import GenerateRandomUserView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url('generate/', GenerateRandomUserView.as_view(), name='generate'),
]

urlpatterns = format_suffix_patterns(urlpatterns)