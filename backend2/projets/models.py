from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from motifs.models import Motifs
from observation.models import Observation
from entreprise.models import Entreprise
# Create your models here.
class Projects(models.Model):

    # Constantes des états de grant:


    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    ref = models.CharField(unique=True, max_length=255, null=False, blank=False)
    projet = models.CharField(unique=True, max_length=255, null=False, blank=False)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.SET_NULL, null=True)
    etat_projet = models.BooleanField(null=False)
    entree = models.DateTimeField(null=True)
    livree = models.DateTimeField(null=True)
    code_fichier = models.CharField(unique=True, max_length=255, null=False)
    phone = models.CharField(max_length=100, null=False, blank=False)
    observation = models.ForeignKey(Observation, on_delete=models.SET_NULL, null=True)
    motifs = models.ManyToManyField(Motifs, blank=True)
        

    class Meta:
        db_table = 'projects'
