from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User 

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']  # Add all the fields you want to include
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# class UserLoginSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length = 255)
#     class Meta:
#         model = User
#         fields = ['username', 'password']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
