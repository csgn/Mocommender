from django.contrib import admin
from django.db import models


class McCrew(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    employee_id = models.IntegerField()
    department = models.CharField(max_length=512)
    job = models.CharField(max_length=512)
    name = models.CharField(max_length=512)
    gender = models.SmallIntegerField()
    profile_path = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'mccrew'


@admin.register(McCrew)
class McCrewAdmin(admin.ModelAdmin):
    pass
