# Generated by Django 5.1.2 on 2024-10-16 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_members_age_alter_members_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='members',
            new_name='member',
        ),
    ]
