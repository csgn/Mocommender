from django.db import models

from movie.models.mcmetadata import McMetadata

class McUser(models.Model):
    username = models.CharField(max_length=32)
    is_active = models.BooleanField()

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'mcuser'




