import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.serializers import serializers
from app.services.user_registration_service import UserRegistrationService


class UserRegistrationView(APIView):
    serializer_class = serializers.UserSerializer

    def get(self, request):
        return Response({"message": "Hello World!"})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        user_reg_service = UserRegistrationService()
        user_reg_service.create_user(serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)
