from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ChatUser(User):
    """
    Custom User model to authenticate users without password
    """
    active = models.BooleanField(default=False)
    password = None