# Create your views here.
# users/views.py
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from note_app.serializer import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer