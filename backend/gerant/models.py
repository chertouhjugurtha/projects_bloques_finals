from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# Create your models here.
class Gerant(models.Model):

    # Constantes des états de grant:


    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nom = models.CharField(unique=True, max_length=255, null=False, blank=False)
    prenom = models.CharField(unique=True, max_length=255, null=False, blank=False)
    age = models.IntegerField(unique=True, validators=[MinValueValidator(1)], null=False)
    date_naissance = models.DateField(null=True)
    phone = models.CharField(max_length=100, null=False, blank=False)
    nationalite = models.CharField(max_length=100,null=False, blank=False)
    gerant = models.BooleanField(null=False)
        

    class Meta:
        db_table = 'grant'
