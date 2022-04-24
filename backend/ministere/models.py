from email.headerregistry import Address
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator,RegexValidator
import uuid
# Create your models here.

# Create your models here.
class Ministere(models.Model):

    # Constantes des états de grant:


    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    ministere = models.CharField(unique=True, max_length=255, null=False, blank=False)
    address = models.CharField( max_length=255, null=False, blank=False)

    class Meta:
        db_table = 'ministere'