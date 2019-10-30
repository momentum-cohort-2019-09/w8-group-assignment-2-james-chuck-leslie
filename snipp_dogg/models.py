from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_description = models.TextField()
    pinned_snippets = models.ManyToManyField(
        to='CodeSnippet',
        related_name='user_pinned',
        blank=True)

    def __str__(self):
        return self.email

class CodeSnippet(models.Model):
    description = models.CharField(max_length=255)
    body = models.TextField()
    language = models.CharField(max_length=15)
    user = models.ForeignKey(
        to=User,
        related_name='user',
        on_delete=models.SET_NULL,
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
