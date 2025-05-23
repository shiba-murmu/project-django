from django.db import models

# Create your models here.

class Register(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.firstname} - {self.lastname} - {self.email}"