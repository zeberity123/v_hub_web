from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .models import CustomUser
from .serializers import UserSerializer, SigninSerializer

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

class SigninView(generics.GenericAPIView):
    serializer_class = SigninSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user is not None:
            login(request, user)
            return Response({"message": "Successfully signed in."})
        return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
