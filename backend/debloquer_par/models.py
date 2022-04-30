from django.db import models
import uuid
from motifs.models import Motifs
from projets.models import Projets

class Debloquer_Par(models.Model):
    LEVES = 'levés'
    NON_LEVES = 'Non levés'
    
    OBSERVATION = [
        (LEVES, 'leves'),
        (NON_LEVES, 'non_leves'),
        
    ]
    # Constantes des états de grant:
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    saisie_par=models.CharField(unique=True, max_length=255, null=False, blank=False)
    motif = models.ForeignKey(Motifs, on_delete=models.CASCADE)
    projets = models.ForeignKey(Projets, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    lever= models.CharField(max_length=100, choices=OBSERVATION, null=False)
    detail_obs=models.CharField(max_length=255, null=True )
  
    
        

    class Meta:
        db_table = 'debloquer_par'