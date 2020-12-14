# Generated by Django 3.1.4 on 2020-12-14 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, unique=True)),
                ('description', models.TextField()),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GlobalSubCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('options', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GuildCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, unique=True)),
                ('guild_id', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='GuildSubCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=180, unique=True)),
                ('username', models.CharField(max_length=180)),
                ('avatar', models.CharField(max_length=180)),
                ('discriminator', models.IntegerField()),
                ('public_flags', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=180)),
                ('extra_data', models.TextField(max_length=180)),
            ],
        ),
    ]