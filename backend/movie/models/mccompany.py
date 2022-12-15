from django.contrib import admin
from django.db import models


class McCompany(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mccompany'


@admin.register(McCompany)
class McCompanyAdmin(admin.ModelAdmin):
    pass
