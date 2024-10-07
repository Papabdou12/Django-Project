from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# models.py

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')

    def __str__(self):
        return f'{self.username} ({self.get_user_type_display()})'
