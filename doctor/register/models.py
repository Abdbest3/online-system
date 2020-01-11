from django.db import models

# Create your models here.
class online(models.model):
    Username = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    pass1 = models.CharField(max_length=20)
    date_of_birth = models.DateField(max_length=10)
    