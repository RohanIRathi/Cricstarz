# Generated by Django 3.1.1 on 2020-10-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_auto_20200926_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='no_of_players',
            field=models.IntegerField(default=0, verbose_name='No. of players per team'),
        ),
    ]
