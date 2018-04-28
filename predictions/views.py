# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from helpers import is_request_valid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test_slack_json(request):
    if not is_request_valid(request):
        return HttpResponseBadRequest()

    request_text = request.POST.get("text")

    return JsonResponse({
        "response_type": 'in_channel',
        "text": response_text
        })
