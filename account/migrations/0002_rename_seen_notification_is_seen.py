# Generated by Django 4.2.4 on 2023-09-14 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='seen',
            new_name='is_seen',
        ),
    ]
