from django.db import models


class McMetadataKeyword(models.Model):
    metadata = models.ForeignKey('McMetadata', on_delete=models.CASCADE)
    keyword = models.ForeignKey('McKeyword', on_delete=models.CASCADE)

    class Meta:
        db_table = "mcmetadatakeyword"
        unique_together = (('metadata', 'keyword'),)

