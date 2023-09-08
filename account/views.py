from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, LoginSerializer
from django.http import HttpResponse
from django.urls import reverse

# , UserLoginSerializer

from django.contrib.auth import authenticate, login, logout

# Create your views here.
class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserLoginView(APIView):
#     def post(self, request, formate=None):
#         serializer = UserLoginSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             # user = serializer.save()
            
#             username = serializer.data.get('username')
#             password = serializer.data.get('password')
#             user = authenticate(username = username, password = password)
#             if user is not None:
#                 return Response({'msg':'login successful'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'errors':{'non_field_errors':['username or password is not valid']}}, status= status.HTTP_404_NOT_FOUND)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    print('*******In the LoginView')
    def post(self, request, formate=None):
        serializer = LoginSerializer(data = request.data)
        print("====================================================================", request.data)
        if serializer.is_valid(raise_exception=True):
            # user = serializer.save()
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                # return Response({'msg':'login successful'}, status=status.HTTP_200_OK)
                print('====================================================================================================',username)
                context = {'username':username}
                return redirect('group_index', group_name = username)
            else:
                return Response({'errors':{'non_field_errors':['username or password is not valid']}}, status= status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

def login_page(request):
    print('**********In the login_page')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponse("logout")
