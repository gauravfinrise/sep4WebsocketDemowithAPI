# topic- chat app with static group name
import json
from channels.consumer import  SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from asgiref.sync import async_to_sync, sync_to_async
from .models import *
from django.contrib.auth.models import User

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connected....', event)
        print('channel_layer...', self.channel_layer) #getdefault channel layer from project 
        print('channel_name...', self.channel_name) #getdefault channel layer name from project 

        # add channel in new or existing group
        async_to_sync(self.channel_layer.group_add)('programmers', self.channel_name)

        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self, event):
        # print('message received from client....', event['text'])
        # print('type of message received from client....', type(event['text']))
        async_to_sync(self.channel_layer.group_send)('programmers',{
            'type':'chat.message',
            'message':event['text']
        })
    def chat_message(self, event):
        # print('Actual data...', event['message'])
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })

    def websocket_disconnect(self, event):
        # print('websocket disconnected....', event)

        # print('channel_layer...', self.channel_layer) #getdefault channel layer from project 
        # print('channel_name...', self.channel_name) #getdefault channel layer name from project 

        async_to_sync(self.channel_layer.group_discard)('programmers', self.channel_name)
        raise StopConsumer()
    
@database_sync_to_async
def get_group_by_name(group_name):
    return Group.objects.get(name=group_name)

class MyAsyncConsumer(AsyncConsumer):
   
    async def websocket_connect(self, event):
        # print('websocket connected....', event)
        # print('channel_layer...', self.channel_layer) #getdefault channel layer from project 
        # print('channel_name...', self.channel_name) #getdefault channel layer name from project 
        # print("group name....",self.scope['url_route']['kwargs']['groupname'])
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        # self.group_name2 = "notification"

        # print("===============================",self.group_name)
        # print("===============================",self.channel_name)
        # channelname = self.channel_name

        # add channel in new or existing group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        # await self.channel_layer.group_add(self.group_name2, self.channel_name)
        # await self.accept()
        await self.send({
            'type':'websocket.accept',         
            # 'channel_name':channelname
        })

        await self.send({
            'type':'websocket.send',
            'text':json.dumps({"groupname":self.channel_name})
        })
        # print("asdgsdfgsdfgsdfgsdfgsdfgsdfgsdfgsdfgsdgsg ========= ",self.group_name)
        # await self.send(text_data=json.dumps({'channel_name': self.channel_name}))
    async def websocket_receive(self, event):
        # print('message received from client....', event['text'])
        # print('type of message received from client....', type(event['text']))
        data = json.loads(event['text'])
        print("data:=========", data)
        # print("=============================-----------------=================")
        # print("data.......", data)
        # print("type of data.......", type(data))
        # print("chart messsage.......", data['msg'])
        # print("=============================-----------------=================")
        
        # Find group object                       
        group = await get_group_by_name(self.group_name)
        # group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
        # group = await sync_to_async(Group.objects.get)(name=self.group_name)
        # print(self.scope['user'])
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",group)
        if self.scope['user'].is_authenticated:
            #create new chat object
            chat = Chat(
                content = data['msg'],
                group = group
            )
            await database_sync_to_async(chat.save)()
            await self.channel_layer.group_send(self.group_name,{
                'type':'chat.message',
                'message':event['text']
            })
        else:
            # print("=======================================================================================")
            self.send({
                'type':'websocket.send',
                'text':json.dumps({"msg":"Login required"})
                # 'text': "Login required"
            })
    
    async def user_registered(self, event):
        print("send notification ==================================***")
        print(event)
        print("send notification ==================================***")

    async def chat_message(self, event):
        # print('Actual data...', event['message'])
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })

    async def websocket_disconnect(self, event):
        # print('websocket disconnected....', event)
        # print('channel_layer...', self.channel_layer) #getdefault channel layer from project 
        # print('channel_name...', self.channel_name) #getdefault channel layer name from project 

        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        raise StopConsumer()


    # Helper function to get all existing users
    @database_sync_to_async
    def get_all_users():
        return User.objects.all()

    # Helper function to add existing users in group
    async def add_existing_users_to_groups(self,group_name2):
        all_users = await self.get_all_users()
        for user in all_users:
            channel_name = f"user_{user.id}"
            await self.channel_layer.group_add(group_name2, channel_name)

from channels.generic.websocket import AsyncWebsocketConsumer

class TestConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data = json.dumps({'status':'connected from django channels'}))
        print(f"User {self.scope['user']} connected to {self.room_group_name} ===================")
    async def receive(self, text_data):
        print(text_data)
        
    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(f"User {self.scope['user']} disconnected to {self.room_group_name}")
        print('disconnected')
    
    async def send_notification(self, event):
        print('================= send notification')
        print(event)
        # print(event.get('value'))
        # data = json.loads(event.get('message'))
        data = (event.get('message'))
        print(data)

        await self.send(text_data=json.dumps({'payload':data}))
        print('================= send notification')
    