# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import Django stuff
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# import models
from django.contrib.auth.models import User
from models import Profile, Prediction

# import helpers
from helpers import is_request_valid, parse_prediction


@csrf_exempt
def test_slack_json(request):
    if not is_request_valid(request):
        return HttpResponseBadRequest()

    request_text = request.POST.get("text")
    parsed = parse_prediction(request_text)

    # save new prediction object
    slack_id = request.POST.get("user_id")
    request_user = Profile.objects.select_related("user").filter(slack_id=slack_id)[0].user
    this_prediction = Prediction(
        user =  request_user,
        description = parsed["description"],
        status = "Awaiting Evaluation",
        horizon = parsed["horizon"]
    )
    this_prediction.save()

    # write back to the user
    response_text = "You predicted that:\n" +\
        "*prediction:*\t" + parsed["description"] + "\n" + \
        "*horizon:*\t\t" + str(parsed["horizon"]) + "\n" + \
        "*tags:*\t\t\t" + str(parsed["tags"])

    return JsonResponse({
        "response_type": 'in_channel',
        "text": response_text
        })
