from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, user_name, name, email, phone, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff = True")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser = True")

        return self.create_user(user_name, name, email, phone, password, **other_fields)

    def create_user(self, user_name, name, email, phone, password, **other_fields):

        if not name:
            raise ValueError(_('Name is a mandatory field'))
        if not email:
            raise ValueError(_('Email is a mandatory field'))

        # email = self.normalize_email(email)
        user = self.model(user_name=user_name,
                          name=name,
                          email=email,
                          phone=phone,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractUser):
    user_name = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, unique=False)
    email = models.EmailField(_('email_address'), max_length=200, unique=True)
    phone = models.IntegerField(null=True)
    start_date = models.DateTimeField(default=timezone.now)

    # include the function create_user from class CustomAccountManager
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.user_name
