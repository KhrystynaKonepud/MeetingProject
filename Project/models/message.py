from django.db import models
from Project.models.chatRoom import ChatRoom
from Project.models.user import User


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="chat_files/", blank=True, null=True)