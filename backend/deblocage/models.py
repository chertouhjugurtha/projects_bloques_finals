from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from models.debloqueur import Debloqueur



class Deblocage(models.Model):
    debloqueur = models.ForeignKey(Debloqueur, on_delete=models.CASCADE)
    deblocage = models.ForeignKey(Deblocage, on_delete=models.CASCADE)
    date_deblocage = models.DateField(null=true)
    
    class Meta:
        db_table = 'deblocage'