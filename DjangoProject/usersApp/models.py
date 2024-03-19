from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to="images/", null=True)
    description = models.CharField(max_length=400, null=True)
    pass