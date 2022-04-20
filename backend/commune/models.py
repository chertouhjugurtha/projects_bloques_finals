from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from wilaya.models import Wilaya
# Create your models here.
# Create your models here.
class Commune(models.Model):

    # Constantes des états de grant:


    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    commune = models.CharField(unique=True, max_length=255, null=False, blank=False)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.SET_NULL, null=True)
    code_postal= models.CharField(unique=True, max_length=255, null=False, blank=False)
    
    class Meta:
        db_table = 'commune'
