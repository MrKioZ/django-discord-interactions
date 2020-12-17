from .variables import InteractionEndPoint, InteractionResponseType
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
import requests

class GlobalCommandStorage(models.Model):
    name = models.CharField(max_length=180, unique=True)
    uid = models.CharField(max_length=180, unique=True, blank=True, null=True)
    description = models.CharField(max_length=180)

    def __str__(self):
        return self.name

class GlobalSubCommandStorage(models.Model):
    name = models.CharField(max_length=180)
    uid = models.CharField(max_length=180)
    master_command = models.ForeignKey(GlobalCommandStorage, on_delete=models.CASCADE)
    options = models.TextField()

    def __str__(self):
        return self.name

class GuildCommandStorage(models.Model):
    name = models.CharField(max_length=180, unique=True)
    guild_id = models.CharField(max_length=180)

    def __str__(self):
        return self.name

class GuildSubCommandStorage(models.Model):
    name = models.CharField(max_length=180)

    def __str__(self):
        return self.name

class Member(models.Model):
    uid = models.CharField(max_length=180, unique=True)
    username = models.CharField(max_length=180)
    avatar = models.CharField(max_length=180)
    discriminator = models.IntegerField()
    public_flags = models.IntegerField()

    def __str__(self):
        return self.username

class Message(models.Model):

    token = models.CharField(max_length=180)
    extra_data = models.TextField(max_length=180)

@receiver(post_save, sender=GlobalCommandStorage)
def save_global_command(sender, instance, **kwargs):
    
    if not instance.uid is None:
        return

    data = {
        "name": instance.name,
        "description": instance.description,
        "options": []
    }

    r = requests.post(InteractionEndPoint.GLOBAL_URL, headers=InteractionEndPoint.headers, json=data)
    r = r.json()

    instance.uid = r.get('id')
    instance.save()

@receiver(pre_delete, sender=GlobalCommandStorage)
def delete_global_command(sender, instance, **kwargs):
    r = requests.delete(InteractionEndPoint.GLOBAL_URL+'/'+instance.uid, headers=InteractionEndPoint.headers)
    print(r)