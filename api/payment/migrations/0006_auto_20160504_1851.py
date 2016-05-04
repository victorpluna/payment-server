# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_payment_card_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
