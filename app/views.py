from django.shortcuts import render
from .consumers import MyAsyncConsumer
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from app.renderers import UserRenderer
from .serializers import *
from rest_framework.response import Response
from account.models import Notification
# Create your views here.

def index(request, group_name):
    # print("Group name ... ", group_name)
    
    print(group_name)
    group = Group.objects.filter(name = group_name).first()
    # print("******************************************************************",group)
    user = request.user
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..", user.username)
    notifications = Notification.objects.filter(user=user)
    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.", notifications)
    chats =[]
    if group:
        chats = Chat.objects.filter(group=group)
    else:
        group = Group(name = group_name)
        group.save()

    # print("======================================================================= group name=",group_name)
    return render(request, 'app/index.html',{'groupname': user.username, 'chats':chats, 'notifications':notifications})

# class UserRegistrationView(APIView):
#     renderer_classes = [UserRenderer]
#     def post(self, request, formate=None):
#         serializer = UserRegistrationSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.save()
#             return Response({'msg':'registration successful'}, status=status.HTTP_201_CREATED)
#         return Response({'msg':'registration faild'}, status=status.HTTP_400_BAD_REQUEST)
