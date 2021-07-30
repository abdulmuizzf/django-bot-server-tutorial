from django.contrib.auth.backends import ModelBackend

from .models import ChatUser

class PasswordlessAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, **kwargs):
        """
        Returns existing user instance if it exists,
        creates a new user otherwise
        """
        if not(username):
            return None
        try:
            user = ChatUser.objects.get(username=username)
        except ChatUser.DoesNotExist:
            user = ChatUser.objects.create(username=username)
        return user
    
    def get_user(self, username):
        try:
            return ChatUser.objects.get(pk=username)
        except ChatUser.DoesNotExist:
            return None