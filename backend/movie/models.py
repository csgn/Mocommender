# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.









# class McMetadataCast(models.Model):
#     metadata_id = models.IntegerField(blank=True, null=True)
#     cast_id = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'mc_metadata_cast'
#
#
# class McMetadataCompany(models.Model):
#     metadata_id = models.IntegerField(blank=True, null=True)
#     company_id = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'mc_metadata_company'
#
#
# class McMetadataCountry(models.Model):
#     metadata_id = models.IntegerField(blank=True, null=True)
#     country_id = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'mc_metadata_country'
#
#
# class McMetadataCrew(models.Model):
#     metadata_id = models.IntegerField(blank=True, null=True)
#     crew_id = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'mc_metadata_crew'
#
#
# class McMetadataGenre(models.Model):
#     metadata = models.OneToOneField(McMetadata, models.DO_NOTHING, primary_key=True)
#     genre = models.ForeignKey(McGenre, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'mc_metadata_genre'
#         unique_together = (('metadata', 'genre'),)
#
#
# class McMetadataKeyword(models.Model):
#     metadata_id = models.TextField(blank=True, null=True)
#     keyword_id = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'mc_metadata_keyword'
#
#
# class McMetadataLanguage(models.Model):
#     metadata_id = models.IntegerField(blank=True, null=True)
#     language_id = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'mc_metadata_language'
