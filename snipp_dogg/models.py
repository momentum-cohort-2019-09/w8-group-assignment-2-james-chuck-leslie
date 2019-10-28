from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    profile_description = models.TextField()

class Created_Snips:
    snip = models.TextField()
    user = models.IntegerField()
    description = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    time_created = models.DateTimeField(default=timezone.now)
    time_updated = models.DateTimeField(default=timezone.now)
