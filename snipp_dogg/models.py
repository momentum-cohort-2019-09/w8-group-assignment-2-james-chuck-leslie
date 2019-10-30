from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    profile_description = models.TextField()

    def __str__(self):
        return self.email

class Language(models.Model):
    name = models.CharField(max_length=255)
    extension = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.name} ({self.extension})"

class CodeSnippet(models.Model):
    description = models.CharField(max_length=255)
    body = models.TextField()
    language = models.CharField(max_length=255)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        related_name='user',
        null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    source = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='derivatives')

    def __str__(self):
        return self.description
