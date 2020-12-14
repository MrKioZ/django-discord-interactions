from django.db import models
from django.conf import settings
import requests, json

# url = "https://discord.com/api/v8/applications/{}/commands"

# headers = {
#     "Authorization": 'Bot {}'.format(settings.DISCORD_INTERACTION_BOT_TOKEN)
# }

# r = requests.post(url, headers=headers, json=json)

class GlobalCommand(models.Model):
    name = models.CharField(max_length=180, unique=True)
    description = models.TextField()
    type = models.IntegerField()

    def save(self, *args, **kwargs):

        # json = {
        #     "name": "blep",
        #     "description": "Send a random adorable animal photo",
        #     "options": [
        #         {
        #             "name": "animal",
        #             "description": "The type of animal",
        #             "type": 3,
        #             "required": True,
        #             "choices": [
        #                 {
        #                     "name": "Dog",
        #                     "value": "animal_dog"
        #                 },
        #                 {
        #                     "name": "Cat",
        #                     "value": "animal_dog"
        #                 },
        #                 {
        #                     "name": "Penguin",
        #                     "value": "animal_penguin"
        #                 }
        #             ]
        #         },
        #         {
        #             "name": "only_smol",
        #             "description": "Whether to show only baby animals",
        #             "type": 5,
        #             "required": False
        #         }
        #     ]
        # }


        super().save(*args, **kwargs)

class GlobalSubCommand(models.Model):
    name = models.CharField(max_length=180)

class GuildCommand(models.Model):
    name = models.CharField(max_length=180, unique=True)
    guild_id = models.CharField(max_length=180)

class GuildSubCommand(models.Model):
    name = models.CharField(max_length=180)