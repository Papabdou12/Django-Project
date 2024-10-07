# users/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'user_type')
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            user_type=validated_data['user_type'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'user_type')

class AdminProfileSerializer(serializers.ModelSerializer):
    # Ajoutez ici les champs spécifiques au profil enseignant
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_type')
        # Ajoutez d'autres champs spécifiques si nécessaire 

class TeacherProfileSerializer(serializers.ModelSerializer):
    # Ajoutez ici les champs spécifiques au profil enseignant
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_type')
        # Ajoutez d'autres champs spécifiques si nécessaire

class StudentProfileSerializer(serializers.ModelSerializer):
    # Ajoutez ici les champs spécifiques au profil étudiant
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_type')
        # Ajoutez d'autres champs spécifiques si nécessaire                