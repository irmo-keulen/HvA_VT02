# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textEdit', '0005_auto_20181127_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='date_pub',
            new_name='date_added',
        ),
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(to='textEdit.Topic'),
        ),
    ]
