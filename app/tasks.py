from celery import shared_task
from django.core.mail import send_mail
from core import settings
# import pywhatkit


@shared_task
def send_email_user(name: str, email: str) -> None:
    send_mail("Register notification",
              "Welcome to our family, " + name + "!",
              settings.EMAIL_HOST_USER,
              [email])


@shared_task
def send_email_department(name: str, email: str, topic: str) -> None:
    send_mail("Selected topic", name + " has selected the topic " + topic,
              settings.EMAIL_HOST_USER,
              [email])


@shared_task
def send_whatsapp(name: str, number: str, topic: str) -> None:
    # Commented due to problems with the library pywhatkit
    # pywhatkit.sendwhatmsg(number, name + " has selected the topic " + topic)
    # Replaced by a print in order to test that it should work
    print(number + " " + name + " has selected the topic " + topic)
