from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length= 50)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__ (self):
        return self.firstname+" "+self.lastname