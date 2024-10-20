# Generated by Django 5.1.2 on 2024-10-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=4)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField(max_length=13)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
