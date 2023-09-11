from django.shortcuts import render
from .consumers import MyAsyncConsumer
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from app.renderers import UserRenderer
from .serializers import *
from rest_framework.response import Response
# Create your views here.

def index(request, group_name):
    # print("Group name ... ", group_name)
    group = Group.objects.filter(name = group_name).first()
    chats =[]
    if group:
        chats = Chat.objects.filter(group=group)
    else:
        group = Group(name = group_name)
        group.save()
    return render(request, 'app/index.html',{'groupname': group_name, 'chats':chats})

# class UserRegistrationView(APIView):
#     renderer_classes = [UserRenderer]
#     def post(self, request, formate=None):
#         serializer = UserRegistrationSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.save()
#             return Response({'msg':'registration successful'}, status=status.HTTP_201_CREATED)
#         return Response({'msg':'registration faild'}, status=status.HTTP_400_BAD_REQUEST)
