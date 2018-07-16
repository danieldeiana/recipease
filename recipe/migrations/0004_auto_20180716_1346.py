# Generated by Django 2.0.7 on 2018-07-16 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20180716_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='meal',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='recipe.Meal'),
        ),
        migrations.RemoveField(
            model_name='meal',
            name='step',
        ),
        migrations.AddField(
            model_name='meal',
            name='step',
            field=models.ManyToManyField(to='recipe.Step'),
        ),
    ]