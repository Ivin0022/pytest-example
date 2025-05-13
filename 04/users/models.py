from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

from core.models import BaseModel

class UserManager(BaseUserManager):

    def create_user(self, username=None, password=None, email=None, **extra_fields):
    
        if email:
            email = self.normalize_email(email)

        user = self.model(username=username, email=email, **extra_fields)
        extra_fields.setdefault('is_active', True)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, email=None, **extra_fields):
        if not email:
                raise ValueError("Superuser must have an email address")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password=password, email=email, **extra_fields)


class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # ← needed ONLY for createsuperuser
    
    objects = UserManager()

    def __str__(self):
        return self.username