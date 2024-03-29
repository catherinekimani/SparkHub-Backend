from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# Create your models here.
class userAccountsManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users nust have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, name, password=None):
        user = self.create_user(email=email, name=name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class userAuth(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    #CredentialOptions
    challenge = models.TextField(blank=True, null=True)
    display_name = models.TextField(blank=True, null=True)
    ukey = models.TextField(unique=False, blank=True, null=True)
    username = models.TextField(unique=False)
    credential_id = models.TextField(blank=True, null=True)
    sign_count = models.IntegerField(blank=True, null=True)
    public_key = models.TextField(blank=True, null=True)
    
    objects = userAccountsManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self) -> str:
        return self.name

    def get_short_name(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.email