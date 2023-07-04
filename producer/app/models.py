from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_message
from .views import send_message_view

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50),
    event = models.CharField(max_length=20)
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        message = self.username
        send_message.delay(message)