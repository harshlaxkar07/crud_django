# Generated by Django 5.1.2 on 2024-10-18 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_rename_members_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='fname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='lname',
            new_name='lastname',
        ),
    ]
