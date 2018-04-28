# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-28 16:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('predictions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_id', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='standard',
        ),
        migrations.AlterField(
            model_name='prediction',
            name='tags',
            field=models.ManyToManyField(null=True, to='predictions.PredictionTag'),
        ),
    ]