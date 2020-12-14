from django.contrib import admin
from .models import GlobalCommand, GuildCommand, GlobalSubCommand, GuildSubCommand

admin.site.register(GlobalCommand)
admin.site.register(GlobalSubCommand)
admin.site.register(GuildCommand)
admin.site.register(GuildSubCommand)
