from django.db import models


class Room(models.Model):
    room_type = models.CharField(max_length=20)
    room_no = models.IntegerField()
    no_of_beds = models.IntegerField()
    price_of_room = models.CharField(max_length=20)
    is_there_tv = models.BooleanField(blank=True)
    is_there_fridge = models.BooleanField(blank=True)
    is_there_drinks = models.BooleanField(blank=True)
    free_breakfast = models.BooleanField(blank=True)

    def __str__(self):
        return f"{self.room_type}"


class Reservation(models.Model):
    room_booked = models.ForeignKey(Room, on_delete=models.CASCADE, )
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')
    email = models.EmailField(default='')

    def __str__(self):
        return f"{self.first_name} {self.room_booked}"
