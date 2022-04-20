from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
# Create your models here.
class Observation(models.Model):

    # Constantes des états de grant:


    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    commentaire_obs = models.CharField(unique=True, max_length=255, null=False, blank=False)
    observation = models.BooleanField(null=False)
    class Meta:
        db_table = 'observation'