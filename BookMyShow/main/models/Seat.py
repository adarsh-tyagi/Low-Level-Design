from django.db import models
from .BaseModel import BaseModel
from .Auditorium import Auditorium
from .SeatStatus import SeatStatus


class Seat(BaseModel):
    name = models.CharField(max_length=255)
    row = models.IntegerField()
    column = models.IntegerField()
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    seat_status = models.CharField(max_length=255, choices=[(status.name, status.value) for status in SeatStatus])
    