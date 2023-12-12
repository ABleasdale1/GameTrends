from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

