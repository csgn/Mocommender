from django.contrib import admin
from django.db import models


class McKeyword(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mckeyword'


@admin.register(McKeyword)
class McKeywordAdmin(admin.ModelAdmin):
    pass
