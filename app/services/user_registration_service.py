from app.models import CustomAccountManager
from django.contrib.auth import get_user_model
from app.tasks import send_email
from app.models import CustomUser


class UserRegistrationService:

    def create_user(self, validated_data:dict)-> None:
        user = CustomUser.objects.create_user(validated_data["email"], validated_data["name"], validated_data["email"],
                                              validated_data["phone"], "")
        send_email.delay(user.name, user.email)
