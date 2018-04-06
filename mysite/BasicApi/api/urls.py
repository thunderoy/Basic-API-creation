from django.conf.urls import url
from .views import RetrieveUpdateProfile

urlpatterns = [
	url('info/', RetrieveUpdateProfile.as_view()),
	url('gender/',RetrieveUpdateProfile.as_view()),
]