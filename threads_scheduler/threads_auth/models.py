from django.db import models
from django.conf import settings
from django.utils import timezone

class ThreadsToken(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    expires_at = models.DateTimeField()

    def is_valid(self):
        return self.expires_at > timezone.now()