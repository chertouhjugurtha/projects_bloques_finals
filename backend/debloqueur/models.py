from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator,RegexValidator
import uuid
from ministere.models import Ministere
from datetime import datetime

from utilisateurs.models import User

# from utilisateurs.models import User
# from django.contrib.auth.models import User

class Debloqueur(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    # username=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    qualite = models.CharField(unique=True, max_length=255, null=False, blank=False)
    bureau = models.CharField(unique=True, max_length=255, null=False, blank=False)
    ministere=models.ForeignKey(Ministere, on_delete=models.CASCADE)
    
    

    date_joined=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'debloqueur'
        
  