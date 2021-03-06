# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cribs', '0014_auto_20170416_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcribequipments',
            name='icon',
            field=models.ImageField(blank=True, upload_to='cribs/static/crib_equipments_icons/'),
        ),
        migrations.AddField(
            model_name='allhobbies',
            name='icon',
            field=models.ImageField(blank=True, upload_to='cribs/static/hobbies_icons/'),
        ),
        migrations.AddField(
            model_name='allroomequipments',
            name='icon',
            field=models.ImageField(blank=True, upload_to='cribs/static/room_equipments_icons/'),
        ),
    ]
