# Generated by Django 2.0.7 on 2018-07-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0010_remove_meal_user_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='comment',
            field=models.ManyToManyField(blank=True, null=True, to='recipe.Comment'),
        ),
    ]