from django.db import models
from django.contrib.auth.models import User
from main.models import ClassRoom

class Reservation(models.Model):
    room_no = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.IntegerField(default=0)
    personnel = models.IntegerField(default=0)
    purpose = models.TextField(max_length=500)

    def __str__(self):
        return self.user.profile.user_name + "의 예약"

    def wait(self):
        self.status = 0
        self.save()

    def confirm(self):
        self.status = 1
        self.save()

    def update(self):
        self.status = 0
        self.save(force_update=True)

    def request_modify(self):
        self.status = 2
        self.save()

    def request_deny(self):
        self.status=3
        self.save()