from django.db import models
from Project.models.user import User


class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    is_private = models.BooleanField(default=False)
    participants = models.ManyToManyField(User)