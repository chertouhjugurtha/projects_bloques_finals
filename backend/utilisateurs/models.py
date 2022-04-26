from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import  MinValueValidator,RegexValidator


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    # email = models.CharField(max_length=255, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phonenumber = models.CharField(validators=[phone_regex], unique=True, max_length=17, blank=True) 

    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = []
