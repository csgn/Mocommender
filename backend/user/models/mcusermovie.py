from django.db import models

from movie.models.mcmetadata import McMetadata

class McUserMovie(models.Model):
    user = models.ForeignKey('McUser', on_delete=models.CASCADE, db_column="user_id")
    movie = models.ForeignKey(McMetadata, on_delete=models.CASCADE, db_column="movie_id")
    is_played = models.BooleanField()
    is_recommended = models.BooleanField()
    is_liked = models.BooleanField()
    is_saved = models.BooleanField()
    play_runtime = models.FloatField()
    play_date = models.DateField()

    #movie = models.ManyToManyField(McMetadata, db_column="movie_id")


    class Meta:
        managed = False
        db_table = 'mcusermovie'
        #unique_together = (('user', 'movie'))



