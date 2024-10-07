# users /views.py

from rest_framework import generics, permissions
from .serializers import CustomUserSerializer, UserDetailSerializer ,AdminProfileSerializer,StudentProfileSerializer,TeacherProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .permissions import IsAdmin, IsTeacher, IsStudent
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomUserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


# Vue pour le Dashboard Admin
class AdminDashboardView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    serializer_class = UserDetailSerializer

    def get_object(self):
        return self.request.user

# Vue pour le Dashboard Enseignant
class TeacherDashboardView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsTeacher]
    serializer_class = TeacherProfileSerializer

    def get_object(self):
        return self.request.user

# Vue pour le Dashboard Étudiant
class StudentDashboardView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent]
    serializer_class = StudentProfileSerializer

    def get_object(self):
        return self.request.user