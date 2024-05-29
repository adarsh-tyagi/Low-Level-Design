from django.db import models
from .BaseModel import BaseModel


class Actor(BaseModel):
    name = models.CharField(max_length=255)
    