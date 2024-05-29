from django.contrib import admin
from .models.User import User
from .models.Expense import Expense
from .models.Group import Group
from .models.ExpenseOwingUser import ExpenseOwingUser
from .models.ExpensePayingUser import ExpensePayingUser
from .models.Transaction import Transaction

# Register your models here.
admin.site.register(User)
admin.site.register(Expense)
admin.site.register(Group)
admin.site.register(ExpenseOwingUser)
admin.site.register(ExpensePayingUser)
admin.site.register(Transaction)
