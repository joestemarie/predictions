# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 13:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('standard', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=100)),
                ('horizon', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PredictionTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='prediction',
            name='tags',
            field=models.ManyToManyField(to='predictions.PredictionTag'),
        ),
        migrations.AddField(
            model_name='prediction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
