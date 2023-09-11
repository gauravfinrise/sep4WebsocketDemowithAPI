from django.core.management.base import BaseCommand
from django.utils import timezone
from account.models import Notification
from account.models import User  # Import your custom user model

class Command(BaseCommand):
    help = 'Clean up old, seen notifications'

    def handle(self, *args, **kwargs):
        threshold = timezone.now() - timezone.timedelta(days=30)

        # Get a list of user IDs with a login count of 2 or more
        user_ids_to_delete = User.objects.filter(login_count__gte=2).values_list('id', flat=True)

        # Delete notifications that belong to users with a login count of 2 or more
        deleted_count, _ = Notification.objects.filter(user_id__in=user_ids_to_delete, seen=True, created_at__lt=threshold).delete()

        self.stdout.write(self.style.SUCCESS(f'Deleted {deleted_count} old, seen notifications for users with 2 or more logins.'))