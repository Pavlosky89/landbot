from app.tasks import send_email_user
from app.models import CustomUser
from app.utils import constants


class UserRegistrationService:

    def create_user(self, validated_data: dict) -> None:
        user = CustomUser.objects.create_user(validated_data[constants.EMAIL], validated_data[constants.NAME], validated_data[constants.EMAIL],
                                              validated_data[constants.PHONE], "")
        send_email_user.delay(user.name, user.email)

    def get_name_by_username(self, username: str) -> str:
        return CustomUser.objects.get_name_by_username(username)
