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

    def create_user(self, username, name, email, phone, password, **other_fields):

        if not name:
            raise ValueError(_('Name is a mandatory field'))
        if not email:
            raise ValueError(_('Email is a mandatory field'))

        # email = self.normalize_email(email)
        user = self.model(username=username,
                          name=name,
                          email=email,
                          phone=phone,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

    def get_name_by_username(self, username):
        user = CustomUser.objects.get(username__exact="landbottest2@bot.com")
        return user.name


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, unique=False)
    email = models.EmailField(_('email_address'), max_length=200, unique=True)
    phone = models.IntegerField(null=True)
    start_date = models.DateTimeField(default=timezone.now)

    # include the function create_user from class CustomAccountManager
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class NotificationManager(BaseUserManager):

    def create_notification(self, username, via, topic):
        notification = self.model(username=username,
                                  via=via,
                                  topic=topic)
        notification.save()
        return notification

    def get_via_by_topic(self, topic):
        notification = Notification()
        return notification.objects.filter(topic).via


class Notification(models.Model):
    username = models.CharField(max_length=150, unique=False)

    topic = models.CharField(max_length=150, unique=False)
    via = models.CharField(max_length=150, unique=False)
    send_time = models.DateTimeField(default=timezone.now)
    objects = NotificationManager()


