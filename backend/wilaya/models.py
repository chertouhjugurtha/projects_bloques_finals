from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


# Create your models here.
class Wilaya(models.Model):

    # Constantes des états de grant:


    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    wilaya = models.CharField(unique=True, max_length=255, null=False, blank=False)
    code_wilaya = models.CharField(unique=True, max_length=255, null=False, blank=False)

    class Meta:
        db_table = 'wilaya'