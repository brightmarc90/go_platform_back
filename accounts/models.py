from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True)
    
    def __str__(self):
        return self.name
    
class Permission(models.Model):
    action = models.CharField(max_length=64, null=False, unique=True)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.description

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Le champ email est obligatoire')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    username = models.CharField(max_length=128, null=False, unique=True)
    is_superuser = models.BooleanField(default=False, null=False)
    is_staff = models.BooleanField(default=False, null=False)
    role_id = Role.objects.get(name = "Joueur")
    role = models.ForeignKey(Role, on_delete=models.PROTECT, default=role_id.id) # un inscrit est par defaut un joueur

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username
    
class Role_Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    permission = models.ForeignKey(Permission, on_delete=models.PROTECT)
