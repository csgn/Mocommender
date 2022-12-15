from django.db import models


class McMetadataCast(models.Model):
    metadata = models.ForeignKey('McMetadata', on_delete=models.CASCADE)
    cast = models.ForeignKey('McCast', on_delete=models.CASCADE)

    class Meta:
        db_table = "mcmetadatacast"
        unique_together = (('metadata', 'cast'),)

