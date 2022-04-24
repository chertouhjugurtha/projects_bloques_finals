from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator,RegexValidator
import uuid

# Create your models here.
class Gerant(models.Model):

    # Constantes des états de grant:
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nom = models.CharField(unique=True, max_length=255, null=False, blank=False)
    prenom = models.CharField(unique=True, max_length=255, null=False, blank=False)
    username = models.CharField(max_length=100, null=False)
    date_naissance = models.DateField(null=True)
    nationalite = models.CharField(max_length=100,null=False, blank=False)
    gerant = models.BooleanField(null=False)
    email = models.CharField(max_length=100, null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Veuillez introduire votre numéro de téléphone sous  format: '+999999999'. en 15 carataires.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    password = models.CharField(max_length=50,validators=[MinValueValidator(8)], null=False)
        

    class Meta:
        db_table = 'gerant'
