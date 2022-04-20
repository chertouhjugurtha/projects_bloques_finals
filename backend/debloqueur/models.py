from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from ministere.models import Ministere


class Debloqueur(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nom = models.CharField(unique=True, max_length=255, null=False, blank=False)
    prenom = models.CharField(unique=True, max_length=255, null=False, blank=False)
    phone = models.CharField(unique=True, max_length=255, null=False, blank=False)
    qualite = models.CharField(unique=True, max_length=255, null=False, blank=False)
    bureau = models.CharField(unique=True, max_length=255, null=False, blank=False)
        
    ministere=models models.ForeignKey(Ministere, on_delete=models.CASCADE)
    class Meta:
        db_table = 'debloqueur'