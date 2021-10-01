from celery import shared_task
from django.core.mail import send_mail
from core import settings


@shared_task
def send_email(name: str, email: str) -> None:
    send_mail("Register notification",
              "Welcome to our family, " + name + "!",
              settings.EMAIL_HOST_USER,
              [email])