from django.db import models
from django.core.validators import MinValueValidator
import uuid
from commune.models import Commune
from wilaya.models import Wilaya
from motifs.models import Motifs
from observation.models import Observation
from entreprise.models import Entreprise
# Create your models here.
class Projets(models.Model):

    # Constantes des états de grant:
    EN_EXPLOITATION = 'EN_EXPLOITATION'
    NON_MIS_EN_EXPLOITATION = 'NON_MIS_EN_EXPLOITATION'

    NON_LEVES = ''
    
    OBSERVATION = [
        (EN_EXPLOITATION , 'EN_EXPLOITATION'),
        (NON_MIS_EN_EXPLOITATION , 'NON_MIS_EN_EXPLOITATION'),
        
    ]

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    ref = models.CharField(unique=True, max_length=255, null=False, blank=False)
    
    projet = models.CharField(max_length=255, null=False, blank=False)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.SET_NULL, null=True, blank=False)
    etat_projet= models.CharField(max_length=100, choices=OBSERVATION, null=False, blank=False)
    entree = models.DateTimeField(null=True)
    livree = models.DateTimeField(null=True)
    code_fichier = models.CharField(max_length=255, null=False)
    nb_employe_prevus = models.IntegerField(validators=[MinValueValidator(1)], null=False)    
    nb_employe_reel = models.IntegerField(validators=[MinValueValidator(1)], null=False)
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.SET_NULL, null=True)
    statue_projets =models.BooleanField(default=False)
        

    class Meta:
        db_table = 'projets'
