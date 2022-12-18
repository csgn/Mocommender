from django.db import models


class McGenre(models.Model):
    name = models.CharField(max_length=16)


    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'mcgenre'
