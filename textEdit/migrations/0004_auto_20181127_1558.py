# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textEdit', '0003_auto_20181127_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='date_added',
            new_name='date_pub',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='pub_date',
            new_name='pub_added',
        ),
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(to='textEdit.Topic'),
        ),
    ]
