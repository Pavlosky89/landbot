from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.serializers.serializers import NotificationSerializer
from app.services.notification_service import NotificationService


class NotificationView(APIView):
    serializer_class = NotificationSerializer

    '''
        Endpoint to send a notification via Email, Slack, etc, depending on the topic selected by the user
        @request: {username, topic}
    '''
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        notification_service = NotificationService()
        notification_service.send_notification(serializer.validated_data)

        return Response(status=status.HTTP_200_OK)
