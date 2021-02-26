from django.db import models


# Create your models here.
class Message(models.Model):
    username = models.CharField(max_length=120)
    content = models.TextField()
