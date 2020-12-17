from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from discord_interactions.models import GlobalCommandStorage, GlobalSubCommandStorage, GuildCommandStorage
from discord_interactions.variables import InteractionEndPoint

import requests

class ApplicationIDNotFound(Exception):
    """Excxeption Raised when Application ID Is not found under settings.py"""

class BotTokenNotFound(Exception):
    """Exception Raised When there is no Bot Token found under settings.py"""

class ApplicationPublicKeyNotFound(Exception):
    """Exception Raised When there is no Public Key found under settings.py"""

class Command(BaseCommand):
    """Collects all available commands in the current application"""

    def handle(self, *args, **options):

        if settings.DISCORD_INTERACTIONS_APPLICATION_ID is None:
            raise ApplicationPublicKeyNotFound()

        if settings.DISCORD_INTERACTIONS_PUBLIC_KEY is None:
            raise ApplicationPublicKeyNotFound()
        
        if settings.DISCORD_INTERACTIONS_BOT_TOKEN is None:
            raise BotTokenNotFound()

        with requests.get(InteractionEndPoint.GLOBAL_URL, headers=InteractionEndPoint.headers) as r:
            data = r.json()

            print(data)

            if len(data) > 0:

                for command in data:

                    name = command.get('name')
                    uid = command.get('id')
                    try:
                        saved_command = GlobalCommandStorage.objects.get(name=command.get('name'))
                        if saved_command.uid != uid:
                            saved_command.uid = uid
                            saved_command.save()
                    except GlobalCommandStorage.DoesNotExist:
                        params = {
                            'name': command.get('name'),
                            'uid': command.get('id'),
                            'description': command.get('description')
                        }

                        GlobalCommandStorage.objects.create(**params)

                print('Collected All Commands Successfully!')

            else:
                print('There was no Commands found!')