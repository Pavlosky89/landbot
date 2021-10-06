from app.tasks import send_email_user
from app.models import CustomUser


class UserRegistrationService:

    def create_user(self, validated_data: dict) -> None:
        user = CustomUser.objects.create_user(validated_data["email"], validated_data["name"], validated_data["email"],
                                              validated_data["phone"], "")
        send_email_user.delay(user.name, user.email)

    def get_name_by_username(self, username):
        return CustomUser.objects.get_name_by_username(username)
