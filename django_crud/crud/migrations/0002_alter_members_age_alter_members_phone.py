# Generated by Django 5.1.2 on 2024-10-16 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='members',
            name='phone',
            field=models.IntegerField(),
        ),
    ]