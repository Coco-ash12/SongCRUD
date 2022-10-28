from datetime import datetime
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = ('Artiste')
        verbose_name_plural = ('Artistes')


class Song(models.Model):
    artiste_id = models.OneToOneField(Artiste, on_delete=models.CASCADE)
    artistes = models.ForeignKey(Artiste, related_name='artiste', on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Song')
        verbose_name_plural = ('Songs')   
    

class Lyric(models.Model):
    song_artistes = models.OneToOneField(Song, on_delete=models.CASCADE)
    songs = models.ForeignKey(Song, related_name='song', on_delete=models.CASCADE)
    content = models.CharField(max_length=1500)
    song_id = models.CharField(max_length=50)
    
   
    def __str__(self):
        return self.song_id 

    class Meta:
        verbose_name = ('Lyric')
        verbose_name_plural = ('Lyrics')  
