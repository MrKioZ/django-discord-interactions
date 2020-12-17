
from django.conf import settings

class InteractionEndPoint:

    headers = {
        "Authorization": 'Bot {}'.format(settings.DISCORD_INTERACTIONS_BOT_TOKEN)
    }

    GLOBAL_URL = "https://discord.com/api/v8/applications/{}/commands".format(settings.DISCORD_INTERACTIONS_APPLICATION_ID)

    def GUILD_URL(self, GUILD_ID: int):
        return "https://discord.com/api/v8/applications/{}/guilds/{}/commands".format(settings.DISCORD_INTERACTIONS_APPLICATION_ID, GUILD_ID)

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

class GlobalCommand:
    
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.id = kwargs.get('id')
        self.application_id = kwargs.get('application_id')
        self.options = kwargs.get('options')

class GuildCommand:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.id = kwargs.get('id')
        self.guild_id = kwargs.get('guild_id')
        self.application_id = kwargs.get('application_id')
        self.options = kwargs.get('options')

class User:
    
    def __init__(self, *args, **kwargs):
        self.avatar = kwargs.get('avatar')
        self.discriminator = kwargs.get('discriminator')
        self.id = kwargs.get('id')
        self.public_flags = kwargs.get('public_flags')
        self.username = kwargs.get('username')

class Member:
    
    def __init__(self, *args, **kwargs):
        self.deaf = kwargs.get('deaf')
        self.is_pending = kwargs.get('is_pending')
        self.joined_at = kwargs.get('joined_at')
        self.mute = kwargs.get('mute')
        self.nick = kwargs.get('nick')
        self.pending = kwargs.get('pending')
        self.permissions = kwargs.get('permissions')
        self.premium_since = kwargs.get('premium_since')
        self.roles = kwargs.get('roles')
        self.user = User(**kwargs.get('user'))


class InteractionRequest:

    def __init__(self, *args, **kwargs):
        self.channel_id = kwargs.get('channel_id')
        self.guild_id = kwargs.get('guild_id')
        self.id = kwargs.get('id')
        self.member = Member(**kwargs.get('member'))
        self.token = kwargs.get('token')
        self.type = kwargs.get('type')
        self.version = kwargs.get('version')
        self.data = kwargs.get('data')

    def __iter__(self):
        yield "channel_id", self.channel_id
        yield "guild_id", self.guild_id
        yield "id", self.id
        yield "member", self.member
        yield "token", self.token
        yield "type", self.type
        yield "version", self.version
        yield "data", self.data

class Embed:

    def __init__(self, *args, **kwargs):
        self.author = kwargs.get('author')
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.url = kwargs.get('url')
        self.timestamp = kwargs.get('timestamp')
        self.color = kwargs.get('color')
        self.footer = kwargs.get('footer')
        self.type = "rich"

    def __iter__(self):
        yield "author", self.author
        yield "title", self.title
        yield "description", self.description
        yield "url", self.url
        yield "timestamp", self.timestamp
        yield "color", self.color
        yield "footer", self.footer
        yield "type", self.type

class InteractionData:

    def __init__(self, *args, **kwargs):

        self.allowed_mentions = []
        self.content = kwargs.get('content')
        if kwargs.get('embeds'):
            self.embeds = [Embed(**i) for i in kwargs.get('embeds')]
        else:
            self.embeds = []
        self.tts = False

    def __iter__(self):
        yield "allowed_mentions", self.allowed_mentions
        yield "content", self.content
        yield "tts", self.tts

        if self.embeds != []:
            yield "embeds", [dict(i) for i in self.embeds]
        else:
            yield 'embeds', self.embeds

class InteractionResponse:
    
    def __init__(self, *args, **kwargs):
        self.data = InteractionData(**kwargs.get('data'))
        self.type = InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE
    
    def __iter__(self):
        yield "type", self.type
        yield "data", dict(self.data)