# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import Django stuff
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# import models
from django.contrib.auth.models import User
from models import Profile, Prediction, PredictionTag

# import helpers
from helpers import slack_request_valid, parse_prediction
import datetime
import os


@csrf_exempt
def test_slack_json(request):
    if not slack_request_valid(request):
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

    # loop through tags and assign them as appropriate
    for tag in parsed["tags"]:
        this_tag, created = PredictionTag.objects.get_or_create(name = tag)
        this_prediction.tags.add(this_tag)

    # write back to the user
    response_text = "You predicted that:\n" +\
        "*prediction:*\t" + parsed["description"] + "\n" + \
        "*horizon:*\t\t" + str(parsed["horizon"]) + "\n" + \
        "*tags:*\t\t\t" + str(parsed["tags"])

    return JsonResponse({
        "response_type": 'in_channel',
        "text": response_text
        })


def slack_message_action(request):
    # TODO: use the callback ID to parse out that this is a confirmation and then go ahead and
    # mark that prediction based on the status

def api_predictions_for_notification(request):
    if not request.META.get("HTTP_SECRET_KEY"):
        return HttpResponseBadRequest()
    if not request.META.get("HTTP_SECRET_KEY") == os.environ['PREDICTIONS_API_KEY']:
        return HttpResponse('Your secret key is bad and you should feel bad', status=401)
    # set a datetime window of 5 minutes so we're only looking at this iteration
    window_start = datetime.datetime.now()
    window_end = window_start + datetime.timedelta(0,300)

    # get all the predictions in that window that haven't been evaluated
    these_predictions = Prediction.objects.filter(
        status = "Awaiting Evaluation",
        horizon__range = (window_start, window_end)
        )

    output = []
    for prediction in these_predictions:
        output.append({
            "slack_id": prediction.user.profile.slack_id,
            "description": prediction.description,
            "horizon": prediction.horizon,
            "prediction_id": prediction.id
        })

    return JsonResponse(output, safe = False)
