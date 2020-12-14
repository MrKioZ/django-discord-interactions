from django.urls import path
from django.conf import settings

from discord_interactions.views import interactions,
                                        get_all_commands

urlpatterns = [
    path('interactions/', interactions),
]

if settings.DEBUG:
    urlpatterns += [path('/commands', get_all_commands)]