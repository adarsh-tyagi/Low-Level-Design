from django.db import models
from .BaseModel import BaseModel
from .User import User


class Group(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    admins = models.ManyToManyField(User, related_name='group_admins')
    participants = models.ManyToManyField(User, related_name='group_participants')
