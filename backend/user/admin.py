from django.contrib import admin


from user.models.mcuser import McUser
from user.models.mcusermovie import McUserMovie


admin.site.register(McUser)
admin.site.register(McUserMovie)
