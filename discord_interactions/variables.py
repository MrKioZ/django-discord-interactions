class InteractionType:
    
    __slots__ = ('PING', 'APPLICATION_COMMAND')

    PING = 1
    APPLICATION_COMMAND = 2

class InteractionResponseType:

    __slots__ = ('PONG',
                'ACKNOWLEDGE',
                'CHANNEL_MESSAGE',
                'CHANNEL_MESSAGE_WITH_SOURCE',
                'ACKNOWLEDGE_WITH_SOURCE'
            )

    PONG = 1
    ACKNOWLEDGE = 2
    CHANNEL_MESSAGE = 3
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    ACKNOWLEDGE_WITH_SOURCE = 5

class InteractionResponseFlags:

    __slots__ = ('EPHEMERAL')

    EPHEMERAL = 1 << 6