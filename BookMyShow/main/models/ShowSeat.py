from django.db import models
from .BaseModel import BaseModel
from .Show import Show
from .Seat import Seat
from .ShowSeatType import ShowSeatType
from .ShowSeatStatus import ShowSeatStatus


class ShowSeat(BaseModel):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    show_seat_type = models.ForeignKey(ShowSeatType, on_delete=models.CASCADE)
    show_seat_status = models.CharField(max_length=255, choices=[(status.name, status.value) for status in
                                                                 ShowSeatStatus])

    @staticmethod
    def get_all_seats_by_ids(show_seat_ids):
        return ShowSeat.objects.select_for_update().filter(id__in=show_seat_ids)
