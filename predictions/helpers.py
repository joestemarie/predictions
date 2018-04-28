import os
import dateparser
import re

def slack_request_valid(request):
    if hasattr(request, 'form'):
        return False

    request_token = request.POST.get("token")
    request_team_id = request.POST.get("team_id")
    is_token_valid = request_token == os.environ['SLACK_VERIFICATION_TOKEN']
    is_team_id_valid = request_team_id == os.environ['SLACK_TEAM_ID']
    return is_token_valid and is_team_id_valid


def text_to_int(text):
    number_dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
    }
    for key in number_dict:
        text = text.replace(key, str(number_dict[key]))
    return(text)

def parse_horizon_text(horizon_text):
    # convert spelled out numbers
    horizon_text = text_to_int(horizon_text)
    if re.match("([0-9].+) from now", horizon_text):
        horizon_text = "in "+ re.findall("([0-9].+) from now", horizon_text)[0]
    parsed = dateparser.parse(horizon_text)
    return(parsed)

def parse_prediction(prediction_text):
    # parse out hashtags
    hashtags = re.findall("(#[A-z]+)", prediction_text)
    tags = [w.replace('#', '') for w in hashtags]

    # setup regex for the rest of it
    pattern = "(.+) by (.+?)(?=#)"
    regex = re.search(pattern, prediction_text)
    description = regex.group(1)

    # parse the horizon date
    horizon_text = regex.group(2)
    horizon = parse_horizon_text(horizon_text)

    return({
        "description": description,
        "horizon": horizon,
        "tags": tags
    })
