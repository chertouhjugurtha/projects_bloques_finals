from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator,RegexValidator
import uuid
from ministere.models import Ministere
from datetime import datetime


class Debloqueur(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nom = models.CharField(unique=True, max_length=255, null=False, blank=False)
    prenom = models.CharField(unique=True, max_length=255, null=False, blank=False)
    username = models.CharField(max_length=100, null=False)
    qualite = models.CharField(unique=True, max_length=255, null=False, blank=False)
    bureau = models.CharField(unique=True, max_length=255, null=False, blank=False)
    ministere=models.ForeignKey(Ministere, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    password = models.CharField(max_length=50,validators=[MinValueValidator(8)], null=False)
    class Meta:
        db_table = 'debloqueur'
        
  