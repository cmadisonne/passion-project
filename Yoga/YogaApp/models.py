from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Events(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
