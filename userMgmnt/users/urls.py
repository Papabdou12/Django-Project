"""
URL configuration for userMgmnt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import AdminDashboardView, RegisterView, UserDetailView,StudentDashboardView,TeacherDashboardView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)
urlpatterns = [
    
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', UserDetailView.as_view(), name='user_detail'),
    path('api/admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('api/teacher-dashboard/', TeacherDashboardView.as_view(), name='teacher_dashboard'),
    path('api/student-dashboard/', StudentDashboardView.as_view(), name='student_dashboard'),
    # Ajoutez d'autres endpoints si nécessaire
    # Ajoutez d'autres endpoints si nécessaire
]
 