from django.db import models
from Project.models.user import User
import uuid


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.IntegerField(help_text="у хвилинах")
    recording_url = models.URLField(blank=True, null=True)
    room_name = models.CharField(max_length=100, unique=True, blank=True)
    recorded = models.BooleanField(default=False)

    @property
    def meeting_url(self):
        base_url = "https://meet.jit.si/"
        return f"{base_url}{self.room_name}"

    def save(self, *args, **kwargs):
        if not self.room_name:
            self.room_name = str(uuid.uuid4())[:8]  # генеруємо унікальний код довжиною 8 символів
        super().save(*args, **kwargs)