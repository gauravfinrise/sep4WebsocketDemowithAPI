from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete,post_init, post_save, post_delete
from django.core.signals import request_started, request_finished, got_request_exception
from .models import Notification
from .models import UserProfile
from django.utils import timezone

@receiver(post_save, sender=User)
def send_notification_on_user_registration(sender, instance, created, **kwargs):
    if created:
        message = f"New user {instance.username} has registered"
        print(message)
        users = User.objects.exclude(id = instance.id)
        for user in users:
            Notification.objects.create(user=user, message=message)

# @receiver(user_logged_out)
# def update_last_login(sender, request, user, **kwargs):
#     user_profile, created = UserProfile.objects.get_or_create(user=user)
#     user_profile.last_login = timezone.now()
#     user_profile.save()

# from .clean_notifications import Command
# @receiver(user_logged_in)
# def run_management_command_on_login(sender, request, user, **kwargs):
#     # Check if the user has logged in 2 or more times (you can adjust this condition)
#     user_profile, created = UserProfile.objects.get_or_create(user=user)
#     if user_profile.login_count >= 2:
#         # Run your management command
#         management_command = Command()
#         management_command.handle()

# @receiver(user_logged_in, sender=User)
# def login_seccess(sender, request, user, **kwargs):
#     print("=============================================")
#     print("Logged-in Signal... Run Intro...")
#     print("Sender: ", sender)
#     print("Request: ", request)
#     print("User: ", user.username)
#     print(f'kwargs: {kwargs}')
# # user_logged_in.connect(login_seccess, sender=User)

# @receiver(user_logged_out, sender=User)
# def log_out_seccess(sender, request, user, **kwargs):
#     print("=============================================")
#     print("log_out Signal... Run Outro...")
#     print("Sender: ", sender)
#     print("Request: ", request)
#     print("User: ", user)
#     print(f'kwargs: {kwargs}')
# # user_logged_out.connect(log_out_seccess, sender=User)

# @receiver(user_login_failed)
# def login_faild(sender,credentials, request, **kwargs):
#     print("=============================================")
#     print("user_login_failed Signal...")
#     print("Sender: ", sender)
#     print("Request: ", request)
#     print("Credentials: ", credentials)
#     print(f'kwargs: {kwargs}')
# # user_login_failed.connect(login_faild)

# @receiver(pre_save, sender=User)
# def at_beginning_save(sender, instance, **kwargs):
#     print("=============================================")
#     print("Pre save Signal...")
#     print("Sender: ", sender)
#     print("Instance: ", instance)
#     print(f'kwargs: {kwargs}')
# # pre_save.connect(at_beginning_save, sender=User)

# @receiver(post_save, sender=User)
# def at_ending_save(sender, instance, created, **kwargs):
#     if created:
#         print("=============================================")
#         print("Post save Signal...")
#         print("new record")
#         print("Sender: ", sender)
#         print("Instance: ", instance)
#         print("created: ", created)
#         print(f'kwargs: {kwargs}')
#     else:
#         print("=============================================")
#         print("Post save Signal...")
#         print("update record")
#         print("Sender: ", sender)
#         print("Instance: ", instance)
#         print("created: ", created)
#         print(f'kwargs: {kwargs}')
# post_save.connect(at_ending_save, sender=User)


# @receiver(pre_delete, sender=User)
# def at_beginning_delete(sender, instance, **kwargs):
#     print("=============================================")
#     print("Pre Delete Signal...")
#     print("Sender: ", sender)
#     print("Instance: ", instance)
#     print(f'kwargs: {kwargs}')
# # pre_delete.connect(at_beginning_delete, sender=User)

# @receiver(post_delete, sender=User)
# def at_ending_delete(sender, instance, **kwargs):
#         print("=============================================")
#         print("Post Delete Signal...")
#         print("Sender: ", sender)
#         print("Instance: ", instance)
#         print(f'kwargs: {kwargs}')
# # post_delete.connect(at_ending_delete, sender=User)


# @receiver(pre_init, sender=User)
# def at_beginning_init(sender, *arrgs , **kwargs):
#     print("=============================================")
#     print("Pre Init Signal...")
#     print("Sender: ", sender)
#     print("Args: ", arrgs)
#     print(f'kwargs: {kwargs}')
# # pre_init.connect(at_beginning_init, sender=User)

# @receiver(post_init, sender=User)
# def at_ending_init(sender, *arrgs, **kwargs):
#     print("=============================================")
#     print("post Init Signal...")
#     print("Sender: ", sender)
#     print("Args: ", arrgs)
#     print(f'kwargs: {kwargs}')
# # post_init.connect(at_ending_init, sender=User)

# @receiver(request_started)
# def at_beginning_request(sender, **kwargs):
#     print("=============================================")
#     print("at Begining Request...")
#     print("Sender: ", sender)
#     # print("Environ: ", environ)
#     print(f'kwargs: {kwargs}')
# # request_started.connect(at_begining_request)

# @receiver(request_finished)
# def at_ending_request(sender, **kwargs):
#     print("=============================================")
#     print("at ending Request...")
#     print("Sender: ", sender)
#     # print("Environ: ", environ)
#     print(f'kwargs: {kwargs}')
# # request_finished.connect(at_ending_request)

# @receiver(got_request_exception)
# def at_req_exception(sender, request, **kwargs):
#     print("=============================================")
#     print("At request exception...")
#     print("Sender: ", sender)
#     print("Request: ", request)
#     print(f'kwargs: {kwargs}')
# # got_request_exception.connect(at_req_exception)