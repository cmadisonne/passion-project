from django.db import models

# Create your models here.
class SignUp(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name
