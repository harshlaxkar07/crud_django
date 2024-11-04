from django.db import models
from django.core.validators import RegexValidator

class Member(models.Model):
    firstname = models.CharField(max_length=50,
        validators=[RegexValidator(regex='^[a-zA-Z]*$',
        message='Only alphabets are allowed.')])
    lastname = models.CharField(max_length=50,
        validators=[RegexValidator(regex='^[a-zA-Z]*$',
        message='Only alphabets are allowed.')])
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__ (self):
        return self.firstname+" "+self.lastname