from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from deblocage.models import Deblocage
from debloqueur.models import Debloqueur

# Create your models here.
class Motifs(models.Model):

    # Constantes des états de grant:
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    type_contrainte = models.CharField(unique=True, max_length=255, null=False, blank=False)
    detail = models.CharField(unique=True, max_length=255, null=False, blank=False)
    
    deblocage = models.ManyToManyField(Debloqueur, through='Deblocage')
    # deblocage = models.ManyToManyField('self', blank=True, related_name="%(class)s_deblocage", symmetrical=False)
        

    class Meta:
        db_table = 'motifs'