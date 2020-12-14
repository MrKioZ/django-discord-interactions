
from django.conf import settings

class InteractionEndPoint:

    headers = {
        "Authorization": 'Bot {}'.format(settings.DISCORD_INTERACTION_BOT_TOKEN)
    }

    GLOBAL_URL = "https://discord.com/api/v8/applications/{}/commands".format(settings.DISCORD_INTERACTION_APPLICATION_ID)

    def GUILD_URL(self, GUILD_ID: int):
        return "https://discord.com/api/v8/applications/{}/guilds/{}/commands".format(settings.DISCORD_INTERACTION_APPLICATION_ID, GUILD_ID)

class InteractionType:

    PING = 1
    APPLICATION_COMMAND = 2

class InteractionResponseType:

    PONG = 1
    ACKNOWLEDGE = 2
    CHANNEL_MESSAGE = 3
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    ACKNOWLEDGE_WITH_SOURCE = 5

class InteractionResponseFlags:

    EPHEMERAL = 1 << 6