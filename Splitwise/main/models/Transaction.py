from django.db import models
from .BaseModel import BaseModel
from .User import User


class Transaction(BaseModel):
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sender_name')
    receiver = models.ForeignKey(User, on_delete=models.PROTECT, related_name='receiver_name')
    amount = models.FloatField()
