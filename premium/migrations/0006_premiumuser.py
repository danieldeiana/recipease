# Generated by Django 2.0.7 on 2018-07-20 12:05

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('premium', '0005_auto_20180720_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremiumUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
