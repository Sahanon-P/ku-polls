# Generated by Django 3.1.1 on 2020-09-18 09:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 19, 9, 29, 33, 592223, tzinfo=utc), verbose_name='date end'),
        ),
    ]
