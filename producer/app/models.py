from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_message

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        message = instance.username
        send_message.delay(message)