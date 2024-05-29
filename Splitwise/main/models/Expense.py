from django.db import models
from .BaseModel import BaseModel
from .User import User
from .Group import Group


class Expense(BaseModel):
    amount = models.FloatField()
    description = models.CharField(max_length=255, default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='expense_participants')
