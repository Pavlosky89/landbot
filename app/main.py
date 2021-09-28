import json

from rest_framework.views import APIView
from rest_framework.response import Response


class UserRegistrationView(APIView):
    # check if user is already logged
    def get(self, request):
        return Response({"message": "Hello World!"})

    def post(self, request):
        return Response({"message": "Hello World!"})


