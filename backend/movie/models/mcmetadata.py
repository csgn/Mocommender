from django.db import models


class McMetadata(models.Model):
    imdb_id = models.CharField(max_length=9)
    title = models.CharField(max_length=255)
    overview = models.CharField(max_length=512, blank=True, null=True)
    popularity = models.FloatField()
    release_date = models.DateField()
    runtime = models.FloatField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    poster_path = models.CharField(max_length=127, blank=True, null=True)

    genre = models.ManyToManyField('McGenre', through='McMetadataGenre')

    class Meta:
        managed = False
        db_table = 'mcmetadata'


class McMetadataGenre(models.Model):
    metadata = models.ForeignKey('McMetadata', on_delete=models.CASCADE)
    genre = models.ForeignKey('McGenre', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'mcmetadatagenre'
        unique_together = (('metadata', 'genre'))
