from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 추가 필드가 필요한 경우 여기에 정의
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.username