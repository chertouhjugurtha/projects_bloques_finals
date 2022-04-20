from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from debloqueur.models import Debloqueur
from motifs.models import Motifs


class Deblocage(models.Model):
    debloqueur = models.ForeignKey(Debloqueur, on_delete=models.CASCADE)
    motifs = models.ForeignKey(Motifs, on_delete=models.CASCADE)
    date_deblocage = models.DateField()
    
    class Meta:
        db_table = 'deblocage'