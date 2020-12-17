from django.urls import path
from django.conf import settings

from .views import interactions, get_all_commands

urlpatterns = [
    path('', interactions),
]

if settings.DEBUG:
    urlpatterns += [path('commands/', get_all_commands)]