# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slack_id = models.CharField(max_length=100)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class PredictionTag(models.Model):
    """Quick tag object so we can look at different kinds of predictions."""
    name = models.CharField(max_length=200)


class Prediction(models.Model):
    """Main object for predictions made by users."""
    user = models.ForeignKey(User)
    description = models.CharField(max_length=250)
    tags = models.ManyToManyField(PredictionTag, null=True)
    status = models.CharField(max_length=100)
    horizon = models.DateTimeField()
