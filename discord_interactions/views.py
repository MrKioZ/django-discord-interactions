from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings

import requests, json

from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
from nacl.signing import VerifyKey

from django.views.decorators.csrf import csrf_exempt

from .models import GlobalCommandStorage, GlobalSubCommandStorage, GuildCommandStorage, GuildSubCommandStorage

from .variables import *
from .commands import commands_methods

def verify_key(raw_body: str, signature: str, timestamp: str, client_public_key: str):
    message = timestamp.encode() + raw_body
    try:
        vk = VerifyKey(bytes.fromhex(client_public_key))
        vk.verify(message, bytes.fromhex(signature))
        return True
    except Exception as ex:
        print(ex)
        pass
    return False

def get_all_commands(request):
    if request.method == 'GET':
        with requests.get(InteractionEndPoint.GLOBAL_URL, headers=InteractionEndPoint.headers) as r:
            return JsonResponse(r.json(), safe=False)

@csrf_exempt
def interactions(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        signature = request.headers.get('X-Signature-Ed25519')
        timestamp = request.headers.get('X-Signature-Timestamp')
        if not verify_key(request.body, signature, timestamp, settings.DISCORD_INTERACTIONS_PUBLIC_KEY):
            return HttpResponse('Bad request signature', status=401)

        # Automatically respond to pings
        if data.get('type') == InteractionType.PING:

            return JsonResponse({'type': InteractionResponseType.PONG})

        # Gets All Available functions for available commands
        commands_methods_names = [i for i in commands_methods.keys()]
        if data.get('data'):
            if data.get('data').get('name') in commands_methods_names:
                command_method = commands_methods.get(data.get('data').get('name'))
                interaction_obj = InteractionRequest(**data)
                return JsonResponse(dict(command_method(interaction_obj)))
            
            elif Settings.DEBUG:
                default_message = """
                **Congrats on sending your command!**

**NOTE**: To create your first function have a decorator with **@GlobalCommand**
Ex:
```python
@GlobalCommand
def blep(data):
    return {
        "data": {
            "allowed_mentions": [],
            "content": "Congrats on sending your command!",
            "embeds": [],
            "tts": False
        },
        "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE
    }
```
                """
                return JsonResponse({
                    "data": {
                        "allowed_mentions": [],
                        "content": default_message,
                        "embeds": [],
                        "tts": False
                    },
                    "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE
                })
    else:
        return HttpResponse('OK')