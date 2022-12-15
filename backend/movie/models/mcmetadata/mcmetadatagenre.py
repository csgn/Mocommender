from django.db import models


class McMetadataGenre(models.Model):
    metadata = models.ForeignKey('McMetadata', on_delete=models.CASCADE)
    genre = models.ForeignKey('McGenre', on_delete=models.CASCADE)

    class Meta:
        db_table = "mcmetadatagenre"
        unique_together = (('metadata', 'genre'),)

