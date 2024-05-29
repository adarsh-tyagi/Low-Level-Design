from django.db import models
from .BaseModel import BaseModel
from .Theatre import Theatre


class Auditorium(BaseModel):
    name = models.CharField(max_length=255)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
