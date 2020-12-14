from .variables import InteractionEndPoint, InteractionResponseType
from django.db import models
from django.conf import settings
import requests

class GlobalCommand(models.Model):
    name = models.CharField(max_length=180, unique=True)
    description = models.TextField()
    type = models.IntegerField()

    def save(self, *args, **kwargs):

        data = {
            "name": self.name,
            "description": self.description,
            "options": [
                {
                    "name": "animal",
                    "description": "The type of animal",
                    "type": InteractionResponseType.CHANNEL_MESSAGE,
                    "required": True,
                    "choices": [
                        {
                            "name": "Dog",
                            "value": "animal_dog"
                        },
                        {
                            "name": "Cat",
                            "value": "animal_dog"
                        },
                        {
                            "name": "Penguin",
                            "value": "animal_penguin"
                        }
                    ]
                },
                {
                    "name": "only_smol",
                    "description": "Whether to show only baby animals",
                    "type": InteractionResponseType.ACKNOWLEDGE_WITH_SOURCE,
                    "required": False
                }
            ]
        }
        url = InteractionEndPoint(settings.DISCORD_INTERACTIONS_APPLICATION_ID).GLOBAL_URL
        r = requests.post(url, headers=headers, json=json)

        super().save(*args, **kwargs)

class GlobalSubCommand(models.Model):
    name = models.CharField(max_length=180)
    options = models.TextField()

class GuildCommand(models.Model):
    name = models.CharField(max_length=180, unique=True)
    guild_id = models.CharField(max_length=180)

class GuildSubCommand(models.Model):
    name = models.CharField(max_length=180)

class Member(models.Model):
    uid = models.CharField(max_length=180, unique=True)
    username = models.CharField(max_length=180)
    avatar = models.CharField(max_length=180)
    discriminator = models.IntegerField()
    public_flags = models.IntegerField()

class Message(models.Model):

    token = models.CharField(max_length=180)
    extra_data = models.TextField(max_length=180)