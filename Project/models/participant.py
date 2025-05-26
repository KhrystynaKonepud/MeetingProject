from django.db import models
from Project.models.meeting import Meeting
from Project.models.user import User


class Participant(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invited_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)