# Generated by Django 2.0.7 on 2018-07-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0004_premium'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='premium',
            name='user',
        ),
        migrations.AddField(
            model_name='premium',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]