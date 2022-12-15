from django.contrib import admin
from django.db import models


class McCountry(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mccountry'


@admin.register(McCountry)
class McCountryAdmin(admin.ModelAdmin):
    pass
