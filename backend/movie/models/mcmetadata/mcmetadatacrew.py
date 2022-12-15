from django.db import models


class McMetadataCrew(models.Model):
    metadata = models.ForeignKey('McMetadata', on_delete=models.CASCADE)
    crew = models.ForeignKey('McCrew', on_delete=models.CASCADE)

    class Meta:
        db_table = "mcmetadatacrew"
        unique_together = (('metadata', 'crew'),)

