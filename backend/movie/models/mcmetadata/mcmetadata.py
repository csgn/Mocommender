from django.contrib import admin
from django.db import models


class McMetadata(models.Model):
    id = models.IntegerField(primary_key=True)
    imdb_id = models.CharField(max_length=9)
    title = models.CharField(max_length=255)
    overview = models.CharField(max_length=255, blank=True, null=True)
    popularity = models.FloatField()
    release_date = models.DateField()
    runtime = models.FloatField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    genre = models.ManyToManyField('McGenre', through='McMetadataGenre')
    cast = models.ManyToManyField('McCast', through='McMetadataCast')

    def __str__(self):
        return self.title

    class Meta:
        managed=False
        db_table = 'mcmetadata'



@admin.register(McMetadata)
class McMetadataAdmin(admin.ModelAdmin):
    pass
