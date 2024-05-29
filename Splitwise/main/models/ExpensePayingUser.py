from django.db import models
from .BaseModel import BaseModel
from .Expense import Expense
from .User import User


class ExpensePayingUser(BaseModel):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    