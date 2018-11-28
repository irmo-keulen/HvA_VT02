# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textEdit', '0014_auto_20181128_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(to='textEdit.Topic'),
        ),
    ]
