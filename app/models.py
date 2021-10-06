from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from app.utils import constants


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, user_name: str, name: str, email: str, phone: str, password: str, **other_fields):

        other_fields.setdefault(constants.IS_STAFF, True)
        other_fields.setdefault(constants.IS_SUPERUSER, True)
        other_fields.setdefault(constants.IS_ACTIVE, True)

        if other_fields.get(constants.IS_STAFF) is not True:
            raise ValueError(constants.ERROR_USER_001)
        if other_fields.get(constants.IS_SUPERUSER) is not True:
            raise ValueError(constants.ERROR_USER_002)

        return self.create_user(user_name, name, email, phone, password, **other_fields)

    def create_user(self, username: str, name: str, email: str, phone: str, password: str, **other_fields):

        if not name:
            raise ValueError(_())
        if not email:
            raise ValueError(_(constants.ERROR_USER_004))

        # email = self.normalize_email(email)
        user = self.model(username=username,
                          name=name,
                          email=email,
                          phone=phone,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

    def get_name_by_username(self, username: str):
        user = CustomUser.objects.get(username__exact=username)
        return user.name


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, unique=False)
    email = models.EmailField(_(constants.EMAIL_ADDRESS), max_length=200, unique=True)
    phone = models.IntegerField(null=True)
    start_date = models.DateTimeField(default=timezone.now)

    # include the function create_user from class CustomAccountManager
    objects = CustomAccountManager()
    USERNAME_FIELD = constants.EMAIL
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class NotificationManager(BaseUserManager):

    def create_notification(self, username: str, via: str, topic: str):
        notification = self.model(username=username,
                                  via=via,
                                  topic=topic)
        notification.save()
        return notification

    def get_via_by_topic(self, topic: str):
        notification = Notification()
        return notification.objects.filter(topic).via


class Notification(models.Model):
    username = models.CharField(max_length=150, unique=False)

    topic = models.CharField(max_length=150, unique=False)
    via = models.CharField(max_length=150, unique=False)
    send_time = models.DateTimeField(default=timezone.now)
    objects = NotificationManager()


