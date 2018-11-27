# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textEdit', '0004_auto_20181127_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='pub_added',
            new_name='date_added',
        ),
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(to='textEdit.Topic'),
        ),
    ]
