from django.db import models
from .BaseModel import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=255)
