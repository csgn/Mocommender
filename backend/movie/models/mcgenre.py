from django.db import models
from django.contrib import admin


class McGenre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mcgenre'

@admin.register(McGenre)
class McGenreAdmin(admin.ModelAdmin):
    pass
