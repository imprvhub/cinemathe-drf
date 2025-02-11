from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class UserRegistrationLog(models.Model):
    email = models.EmailField()
    registration_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'user_registration_log'

class UserLoginLog(models.Model):
    email = models.EmailField()
    login_date = models.DateTimeField(default=timezone.now)
    success = models.BooleanField(default=True)

    class Meta:
        db_table = 'user_login_log'