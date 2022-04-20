from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from branche.models import Branche

# Create your models here.
class Secteur(models.Model):

    # Constantes des états de grant:


    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    secteur = models.CharField(unique=True, max_length=255, null=False, blank=False)
    branche = models.ForeignKey(Branche, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'secteur'

