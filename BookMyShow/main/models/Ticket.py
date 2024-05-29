from django.db import models
from .BaseModel import BaseModel
from .Show import Show
from .User import User
from .ShowSeat import ShowSeat
from .TicketStatus import TicketStatus


class Ticket(BaseModel):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    show_seat = models.ManyToManyField(ShowSeat)
    total_price = models.FloatField()
    ticket_status = models.CharField(max_length=255, choices=[(status.name, status.value) for status in TicketStatus])
    