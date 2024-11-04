# Generated by Django 5.1.2 on 2024-10-20 16:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_rename_fname_member_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='firstname',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Only alphabets are allowed.', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='lastname',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Only alphabets are allowed.', regex='^[a-zA-Z]*$')]),
        ),
    ]