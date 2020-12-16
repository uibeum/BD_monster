from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nick_name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created", )

    def __str__(self):
        return self.nick_name+"의 정보"