from django.shortcuts import render, JsonResponse
from django.conf import settings

import requests, json

from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
from nacl.signing import VerifyKey

from discord_interactions.models import GlobalCommand,
                                        GlobalSubCommand,
                                        GuildCommand,
                                        GuildSubCommand

from discord_interactions.variables import *

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
        with requests.get('https://discord.com/api/v8/applications/{}/commands'.format(settings.DISCORD_INTERACTION_APPLICATION_ID)) as r:
            data = r.json()
            return JsonResponse(data)

def interactions(request):

    if request.method == 'POST':
        signature = request.headers.get('X-Signature-Ed25519')
        timestamp = request.headers.get('X-Signature-Timestamp')
        if not verify_key(request.data, signature, timestamp, settings.DISCORD_INTERACTION_PUBLIC_KEY):
            return 'Bad request signature', 401

        # Automatically respond to pings
        if request.json and request.json['type'] == InteractionType.PING:
            return JsonResponse({
                'type': InteractionResponseType.PONG
            })

        else:
            return jsonify({
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {
                    "tts": False,
                    "content": "Congrats on sending your command!",
                    "embeds": [],
                    "allowed_mentions": []
                }
            })
