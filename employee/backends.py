from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, USERID=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(USERID=USERID)
        except CustomUser.DoesNotExist:
            return None  # User not found

        if user.check_password(password):
            return user  # Return the user if the password is valid
        else:
            return None  # Password is incorrect

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None
