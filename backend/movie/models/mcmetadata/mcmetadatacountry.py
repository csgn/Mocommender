from django.db import models


class McMetadataCountry(models.Model):
    metadata = models.ForeignKey('McMetadata', on_delete=models.CASCADE)
    country = models.ForeignKey('McCountry', on_delete=models.CASCADE)

    class Meta:
        db_table = "mcmetadatacountry"
        unique_together = (('metadata', 'country'),)

