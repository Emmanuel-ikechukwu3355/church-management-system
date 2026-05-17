from django.db import models
from members.models import Member
from events.models import Event

class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.member} - {self.event}"
