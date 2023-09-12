from django.urls import path
from .import consumers

websocket_urlpatterns = [
    path('ws/sc/', consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/<str:groupname>/', consumers.MyAsyncConsumer.as_asgi()),
]

# # projectname/routing.py
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import re_path
# from notificationapp import consumers

# application = ProtocolTypeRouter({
#     "websocket": URLRouter([
#         re_path(r"ws/notifications/(?P<user_id>\d+)/$", consumers.NotificationConsumer.as_asgi()),
#     ]),
# })


# # notificationapp/consumers.py
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.user_id = self.scope["url_route"]["kwargs"]["user_id"]

#         # Add the user to a group based on their user ID
#         await self.channel_layer.group_add(
#             f"user_{self.user_id}",
#             self.channel_name
#         )

#         await self.accept()

#     async def disconnect(self, close_code):
#         # Remove the user from the group when they disconnect
#         await self.channel_layer.group_discard(
#             f"user_{self.user_id}",
#             self.channel_name
#         )

#     async def send_notification(self, event):
#         message = event["message"]

#         # Send the notification to the WebSocket
#         await self.send(text_data=json.dumps({
#             "message": message
#         }))


# # notificationapp/signals.py
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync

# @receiver(post_save, sender=User)
# def create_notification_on_user_registration(sender, instance, created, **kwargs):
#     if created:
#         message = f"New user {instance.username} is registered."

#         # Send the notification to all WebSocket clients in the user's group
#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             f"user_{instance.id}",
#             {
#                 "type": "send_notification",
#                 "message": message
#             }
#         )


# # notificationapp/signals.py
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync

# @receiver(post_save, sender=User)
# def create_notification_on_user_registration(sender, instance, created, **kwargs):
#     if created:
#         message = f"New user {instance.username} is registered."

#         # Send the notification to all WebSocket clients in the user's group
#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             f"user_{instance.id}",
#             {
#                 "type": "send_notification",
#                 "message": message
#             }
#         )



# <!-- notifications.html -->
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Real-time Notifications</title>
# </head>
# <body>
#     <h1>Notifications</h1>
#     <ul id="notification-list">
#         <!-- Notifications will appear here dynamically -->
#     </ul>

#     <script>
#         const notificationList = document.getElementById('notification-list');
#         const socket = new WebSocket(`ws://your-domain/ws/notifications/${user_id}/`);

#         socket.onmessage = (event) => {
#             const data = JSON.parse(event.data);
#             const notificationItem = document.createElement('li');
#             notificationItem.textContent = data.message;
#             notificationList.appendChild(notificationItem);
#         };
#     </script>
# </body>
# </html>
