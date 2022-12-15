from django.contrib import admin
from django.db import models


class McLanguage(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mclanguage'


@admin.register(McLanguage)
class McLanguageAdmin(admin.ModelAdmin):
    pass
