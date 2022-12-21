from django.db import models

from movie.models.mcmetadata import McMetadata


class McUserRecommend(models.Model):
    user = models.ForeignKey('McUser', models.CASCADE, db_column="user_id" ,related_name="user_id")
    movie = models.ForeignKey(McMetadata, models.CASCADE, db_column="movie_id", related_name="movie_id")
    refer = models.ForeignKey(McMetadata, models.CASCADE, db_column="refer_id", related_name="refer_id")

    class Meta:
        managed = False
        db_table = 'mcuserrecommend'
