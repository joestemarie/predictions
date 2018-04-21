# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class PredictionTag(models.Model):
    """Quick tag object so we can look at different kinds of predictions."""
    name = models.CharField(max_length=200)


class Prediction(models.Model):
    """Main object for predictions made by users."""
    user = models.ForeignKey(User)
    description = models.CharField(max_length=250)
    standard = models.CharField(max_length=250)
    tags = models.ManyToManyField(PredictionTag, null=True)
    status = models.CharField(max_length=100)
    horizon = models.DateTimeField()
