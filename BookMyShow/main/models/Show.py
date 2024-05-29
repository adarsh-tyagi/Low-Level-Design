from django.db import models
from .BaseModel import BaseModel
from .Movie import Movie
from .Auditorium import Auditorium
from .Feature import Feature


class Show(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    show_features = models.CharField(max_length=255, choices=[(feature.name, feature.value) for feature in Feature],
                                     blank=True)
    