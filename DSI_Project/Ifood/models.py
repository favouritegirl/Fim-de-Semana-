from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import User

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('O campo email é obrigatório')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    def get_by_natural_key(self, email):
        return self.get(email=email)


class consumidor(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, unique=True, blank=True, null=True)
    password = models.CharField(max_length=100, unique=True, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

class Endereco(models.Model):
    id = models.IntegerField(primary_key=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    id_consumidor = models.ForeignKey(consumidor, on_delete=models.DO_NOTHING, db_column='consumidor', blank=True, null=False)