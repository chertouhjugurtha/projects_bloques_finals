from django.db import models
import uuid
# Create your models here.
from motifs.models import Motifs
from debloqueur.models import Debloqueur

# Create your models here.
class Deblocage(models.Model):

    # Constantes des états de grant:
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    dt_dablocage = models.CharField(unique=True, max_length=255, null=False, blank=False)
  
    motif = models.ForeignKey(Motifs, on_delete=models.CASCADE)
    deblocage = models.ForeignKey(Debloqueur, on_delete=models.CASCADE)
    # deblocage = models.ManyToManyField(Debloqueur, through='Deblocage')
    #deblocage = models.ManyToManyField(Debloqueur, blank=True, related_name="deblocage")
        

    class Meta:
        db_table = 'deblocages'
