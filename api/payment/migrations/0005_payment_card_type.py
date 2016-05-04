# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20160504_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='card_type',
            field=models.CharField(choices=[(b'visa', b'Visa'), (b'mastercard', b'Mastercard'), (b'diners', b'Diners'), (b'discover', b'Discover'), (b'elo', b'Elo'), (b'amex', b'Amex')], default='visa', max_length=30, verbose_name=b'Bandeira'),
            preserve_default=False,
        ),
    ]
