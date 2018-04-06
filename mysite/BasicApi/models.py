from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Profile(models.Model):
	choices = (
		('M', 'Male'),
		('F', 'Female'),
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	gender = models.CharField(max_length=20, choices=choices, blank=False, default=None)
	address = models.CharField(max_length=100, blank=False)

	mobile_regex = RegexValidator(regex=r'^\d{10}$', message="Mobile number must be entered in the format: '9999999999'. Exactly 10 digits allowed.")
	mobile = models.CharField(validators=[mobile_regex], max_length=10, blank=False)# validators should be a list