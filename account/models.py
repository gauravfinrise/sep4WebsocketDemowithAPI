from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
# # signals.py
# from django.dispatch import Signal

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
# new_user_registerd = Signal


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False) #seen field

    def __str__(self):
        return self.message
    
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     last_login = models.DateTimeField(default=timezone.now)
#     login_count = models.PositiveIntegerField(default=0)
    
#     def __str__(self):
#         return self.user.username