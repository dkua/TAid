# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20170721_1450'),
        ('api', '0002_auto_20170714_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaidEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.Event')),
            ],
            bases=('schedule.event',),
        ),
        migrations.AlterField(
            model_name='practical',
            name='teaching_assistant',
            field=models.ManyToManyField(blank=True, to='api.TeachingAssistant', verbose_name='Teaching Assistant(s)'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='teaching_assistant',
            field=models.ManyToManyField(blank=True, to='api.TeachingAssistant', verbose_name='Teaching Assistant(s)'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.TaidEvent'),
        ),
        migrations.AddField(
            model_name='practical',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.TaidEvent'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.TaidEvent'),
        ),
    ]
