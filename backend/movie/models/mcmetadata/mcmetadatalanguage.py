from django.db import models


class McMetadataLanguage(models.Model):
    metadata = models.ForeignKey('McMetadata', on_delete=models.CASCADE)
    language = models.ForeignKey('McLanguage', on_delete=models.CASCADE)

    class Meta:
        db_table = "mcmetadatalanguage"
        unique_together = (('metadata', 'language'),)

