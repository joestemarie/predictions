import os

def is_request_valid(request):
    if hasattr(request, 'form'):
        return False

    request_token = request.POST.get("token")
    request_team_id = request.POST.get("team_id")
    is_token_valid = request_token == os.environ['SLACK_VERIFICATION_TOKEN']
    is_team_id_valid = request_team_id == os.environ['SLACK_TEAM_ID']
    return is_token_valid and is_team_id_valid
