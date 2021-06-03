from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user, get_user_model


class UserProfileManager(BaseUserManager):
    """ Manager for Users profiles"""

    def create_user(self, email, name, password=None):
        """ Crate New new user """
        if not email:
            """ case if users not put email"""
            raise ValueError('User must have an email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        # user.is_superuser = models.BooleanField(default=True)
        # user.is_staff = models.BooleanField(default=True)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """" Model from Data base for Users in System"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    """ """
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Get full name """
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        """ Return string representing user"""
        return self.name
