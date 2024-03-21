from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", null=True)
    description = models.CharField(max_length=1000, null=True)
    pass