from django.db import models
from .BaseModel import BaseModel
from .Ticket import Ticket
from .PaymentStatus import PaymentStatus
from .PaymentType import PaymentType


class Payment(BaseModel):
    payment_status = models.CharField(max_length=255, choices=[(status.name, status.value) for status in PaymentStatus])
    payment_type = models.CharField(max_length=255, choices=[(payment_type.name, payment_type.value) for payment_type
                                                             in PaymentType])
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    payment_time = models.DateTimeField()
    reference_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
