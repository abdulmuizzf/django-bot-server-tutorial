from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ChatUser(User):
    """
    Custom User model to authenticate users without password
    """
    active = models.BooleanField(default=False)
    password = None

class BotHistory(models.Model):
    """
    Store number of calls for each joke category for each user
    """
    user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    stupid_count = models.IntegerField(default=0)
    fat_count = models.IntegerField(default=0)
    dumb_count = models.IntegerField(default=0)