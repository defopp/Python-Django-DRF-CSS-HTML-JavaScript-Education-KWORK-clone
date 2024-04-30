from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", null=False, default="avatars/avatar.png")
    description = models.CharField(max_length=1000, null=True)
    pass
