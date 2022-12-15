from django.contrib import admin
from django.db import models


class McCast(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    actor_id = models.IntegerField()
    name = models.CharField(max_length=512)
    gender = models.SmallIntegerField()
    cast_id = models.SmallIntegerField(blank=True, null=True)
    cast_character = models.CharField(max_length=512, blank=True, null=True)
    cast_order = models.SmallIntegerField(blank=True, null=True)
    profile_path = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'mccast'


@admin.register(McCast)
class McCastAdmin(admin.ModelAdmin):
    pass
