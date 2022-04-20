
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from gerant.models import Gerant
from commune.models import Commune
from secteur.models import Secteur
# Create your models here.
class Entreprise(models.Model):

    # Constantes des états de grant:


    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    raison_social = models.CharField(unique=True, max_length=255, null=False, blank=False)
    nb_employe_prevus = models.IntegerField(unique=True, validators=[MinValueValidator(1)], null=False)    
    nb_employe_reel = models.IntegerField(unique=True, validators=[MinValueValidator(1)], null=False)
    type_entrp = models.CharField(max_length=100, null=False, blank=False)
    gerant = models.ForeignKey(Gerant, on_delete=models.SET_NULL, null=True)
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True)
    secteur = models.ForeignKey(Secteur, on_delete=models.SET_NULL, null=True)


    class Meta:
        db_table = 'entreprise'
