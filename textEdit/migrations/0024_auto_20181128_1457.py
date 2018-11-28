# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textEdit', '0023_auto_20181128_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(to='textEdit.Topic'),
        ),
    ]
