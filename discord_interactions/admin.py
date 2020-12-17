from django.contrib import admin
from .models import GlobalCommandStorage, GuildCommandStorage, GlobalSubCommandStorage, GuildSubCommandStorage

admin.site.register(GlobalCommandStorage)
admin.site.register(GlobalSubCommandStorage)
admin.site.register(GuildCommandStorage)
admin.site.register(GuildSubCommandStorage)
