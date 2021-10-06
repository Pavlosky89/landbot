import json
from app.services.user_registration_service import UserRegistrationService
from app.tasks import send_whatsapp
from app.tasks import send_email_department
from app.models import Notification


class NotificationService:

    def send_notification(self, validated_data: dict) -> None:
        with open("app/utils/notification_config.json") as configuration_file:
            config = json.load(configuration_file)
        # get input data
        username = validated_data.get('username')
        topic = validated_data.get('topic')
        via = config[validated_data.get('topic')]['via']
        reference = config[validated_data.get('topic')]['ref']

        # search for the name of the user
        user_registration_class = UserRegistrationService()
        name = user_registration_class.get_name_by_username(username)

        # call tasks due to selected topic
        if via == 'email':
            send_email_department.delay(name, reference, topic)
        elif via == 'whatsapp':
            send_whatsapp.delay(name, reference, topic)

        # save notification log in DB
        Notification.objects.create_notification(username, via, topic)


