# from rest_framework import serializers
# from .models import *

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     passwoed2 = serializers.CharField(style = {'input_type' : 'password'}
#                                       ,write_only = True)
#     class Meta:
#         model = User
#         fields = ['email', 'name', 'paswword', 'password2', 'tc']
#         extra_kwargs = {'password':{'write_only':True}}

# # validate password and password2 while registration
#     def validate(self, attrs):
#         password = attrs.get('password')
#         password2 = attrs.get('password2')
#         if password != password2:
#             raise serializers.ValidationError("password and confirm password doesn't match")
#         return attrs

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
#     # 