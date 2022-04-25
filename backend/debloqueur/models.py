from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator,RegexValidator
import uuid
from ministere.models import Ministere


def jwt_get_secret_key(user_model):
    return user_model.jwt_secret

class DebloqueurUserManager(BaseUserManager):
    def create_user(self, email,username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Utilisateur n\'a pas de l\'e-mail')

        user = self.model(
            email=self.normalize_email(email),
        )
        user = self.model(email=email, username=username, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and
        password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Debloqueur(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nom = models.CharField(unique=True, max_length=255, null=False, blank=False)
    prenom = models.CharField(unique=True, max_length=255, null=False, blank=False)
    username = models.CharField(max_length=255, unique=True)
    qualite = models.CharField(unique=True, max_length=255, null=False, blank=False)
    bureau = models.CharField(unique=True, max_length=255, null=False, blank=False)
    ministere=models.ForeignKey(Ministere, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    debloqueur=models.BooleanField(default=False)

    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    jwt_secret = models.UUIDField(default=uuid.uuid4)

    objects = DebloqueurUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username", "nom", "prenom"]


    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

