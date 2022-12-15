from django.db import models


class McMetadataCompany(models.Model):
    metadata = models.ForeignKey('McMetadata', on_delete=models.CASCADE)
    company = models.ForeignKey('McCompany', on_delete=models.CASCADE)

    class Meta:
        db_table = "mcmetadatacompany"
        unique_together = (('metadata', 'company'),)

