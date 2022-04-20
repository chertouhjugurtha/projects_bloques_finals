from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from ministere.models import Ministere
from datetime import datetime
import pytz
cn_tz = pytz.timezone('Asia/Shanghai')

class Debloqueur(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nom = models.CharField(unique=True, max_length=255, null=False, blank=False)
    prenom = models.CharField(unique=True, max_length=255, null=False, blank=False)
    phone = models.CharField(unique=True, max_length=255, null=False, blank=False)
    qualite = models.CharField(unique=True, max_length=255, null=False, blank=False)
    bureau = models.CharField(unique=True, max_length=255, null=False, blank=False)
    date_debloquesss = models.DateTimeField(auto_now=True, default=datetime.now(), blank=True)
    

    ministere=models.ForeignKey(Ministere, on_delete=models.CASCADE)
    class Meta:
        db_table = 'debloqueur'