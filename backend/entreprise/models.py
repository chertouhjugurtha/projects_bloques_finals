
from django.db import models
import uuid
from gerant.models import Gerant
from activite.models import Activite
# Create your models here.
class Entreprise(models.Model):
    # Constantes des états de grant:
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    raison_social = models.CharField(unique=True, max_length=255, null=False, blank=False)
    type_entrp = models.CharField(max_length=100, null=False, blank=False)
    gerant = models.ForeignKey(Gerant, on_delete=models.SET_NULL, null=True)
    secteur = models.ForeignKey(Activite, on_delete=models.SET_NULL, null=True)


    class Meta:
        db_table = 'entreprise'
