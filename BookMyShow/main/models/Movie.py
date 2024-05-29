from django.db import models
from .BaseModel import BaseModel
from .Genre import Genre
from .Actor import Actor


class Movie(BaseModel):
    name = models.CharField(max_length=255)
    actor = models.ManyToManyField(Actor)
    genre = models.CharField(max_length=255, choices=[(genre.name, genre.value) for genre in Genre])
