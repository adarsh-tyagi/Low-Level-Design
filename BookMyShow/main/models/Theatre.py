from django.db import models
from .BaseModel import BaseModel
from .City import City


class Theatre(BaseModel):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField()
