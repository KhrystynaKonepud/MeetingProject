from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True)