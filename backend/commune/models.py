from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from wilaya.models import Wilaya

class Commune(models.Model):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    code_postal= models.CharField(max_length=255,blank=True)
    commune = models.CharField(max_length=255, null=False)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.SET_NULL, null=True)
    address= models.CharField(max_length=255, null=False, blank=False)
    region= models.CharField(max_length=255, null=False, blank=False)
    class Meta:
        db_table = 'commune'
