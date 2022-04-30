import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import  MinValueValidator,RegexValidator,ProhibitNullCharactersValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from motifs.models import Motifs
from projets.models import Projets
from wilaya.models import Wilaya
# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        # if not self.verify_is_integer(email):
        #     raise ValueError('The given email is not an integer')
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields) # using email_id instead of email
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_debloqueur(self,username, email,password, **extra_fields): 
        user = User._create_user(username, email,password, **extra_fields)
        user.is_debloqueur = True
        # user.is_superuser = True
        user.save(using=User._db)
        return user

    def create_superuser(self,username,  email, password, **extra_fields):
        user = self._create_user(username, email,password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    def create_debloqueur(self,username,  email, password, **extra_fields):
        user = self._create_user(username, email,password, **extra_fields)
        user.is_debloqueur = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True, blank=False, null=False)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)


    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phonenumber = models.CharField(validators=[phone_regex],  max_length=17) 
    
    password = models.CharField(max_length=255)
    wilaya=models.ForeignKey(Wilaya,on_delete=models.SET_NULL, null=True,blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    # email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_debloqueur = models.BooleanField(default=False)
    
    
    motifs = models.OneToOneField(Motifs, on_delete=models.SET_NULL, null=True)
    
    

    objects = UserManager()

    # EMAIL_FIELD = 'email'
    name_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name']

