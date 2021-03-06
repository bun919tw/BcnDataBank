# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-18 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BtcPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('open', models.DecimalField(decimal_places=8, max_digits=16)),
                ('close', models.DecimalField(decimal_places=8, max_digits=16)),
                ('high', models.DecimalField(decimal_places=8, max_digits=16)),
                ('low', models.DecimalField(decimal_places=8, max_digits=16)),
                ('volume_btc', models.DecimalField(decimal_places=8, max_digits=20)),
                ('volume_currency', models.DecimalField(decimal_places=8, max_digits=20)),
                ('weighted_price', models.DecimalField(decimal_places=8, max_digits=20)),
            ],
        ),
    ]
