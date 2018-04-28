# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Prediction, PredictionTag, Profile

# Register your models here.
admin.site.register(Prediction)
admin.site.register(PredictionTag)
admin.site.register(Profile)
