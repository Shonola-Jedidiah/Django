from msilib.schema import Class
from turtle import title
from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=12)
    second_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    age = models.IntegerField()


class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, models.CASCADE)
    title = models.CharField(max_length= 30)
    date_released = models.DateField(default=datetime.today)
    likes = models.BigIntegerField()
    artiste_id = models.IntegerField()

class Lyric(models.Model):
    Song = models.ForeignKey(Song, models.CASCADE)
    content = models.CharField(max_length=1000)
    song_Id = models.IntegerField()

