from django.db import models
from Project.models.user import User


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.IntegerField(help_text="у хвилинах")
    recording_url = models.URLField(blank=True, null=True)
    room_name = models.CharField(max_length=100, unique=True)
    recorded = models.BooleanField(default=False)