from django.db import models

class Building(models.Model):
    building_no = models.CharField(max_length=3, primary_key=True)
    building_name = models.CharField(max_length=10)
    min_floor = models.IntegerField(default=0)
    max_floor = models.IntegerField(default=0)

    def __str__(self):
        return self.building_name

class ClassRoom(models.Model):
    building_no = models.ForeignKey(Building, db_column='building_no', on_delete=models.CASCADE)
    room_no = models.CharField(max_length=4)
    floor = models.IntegerField(default=1)
    capacity = models.IntegerField(default=0)

    class Meta:
        unique_together = (("building_no", "room_no"),)

    def __str__(self):
        return self.building_no.building_no + "관" + self.room_no + "호"