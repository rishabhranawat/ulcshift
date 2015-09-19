# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('where', models.CharField(max_length=254)),
                ('courses', models.CharField(max_length=254)),
                ('time', models.CharField(max_length=254)),
                ('pay', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('number_of_subs', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='subs',
            name='by',
            field=models.ForeignKey(related_name='Who', to='shifts.Tutor'),
        ),
        migrations.AddField(
            model_name='subs',
            name='to',
            field=models.ForeignKey(related_name='Whom', to='shifts.Tutor'),
        ),
    ]
