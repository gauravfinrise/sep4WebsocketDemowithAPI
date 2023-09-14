from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
# # signals.py
# from django.dispatch import Signal

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
# new_user_registerd = Signal

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False) #seen field

    # def save(self, *args, **kwargs):
    #     print('save called====================================')
    #     channel_layer = get_channel_layer()
    #     notification_objs = Notification.objects.filter(is_seen=False).count()
    #     data={'count':notification_objs, 'current_notification':self.message}
    #     async_to_sync(channel_layer.group_send)(
    #         'test_consumer_group',{
    #             'type':'send_notification',
    #             'value':json.dumps(data)
    #         }
    #     )
    #     super(Notification, self).save(*args, **kwargs)

    def __str__(self):
        return self.message
    
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     last_login = models.DateTimeField(default=timezone.now)
#     login_count = models.PositiveIntegerField(default=0)
    
#     def __str__(self):
#         return self.user.username