from django.contrib import admin


from user.models.mcuser import McUser
from user.models.mcusermovie import McUserMovie
from user.models.mcuserrecommend import McUserRecommend


admin.site.register(McUser)
admin.site.register(McUserMovie)
admin.site.register(McUserRecommend)
