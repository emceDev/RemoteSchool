from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)

    
