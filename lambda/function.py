from slackclient import SlackClient
import requests
import os

def send_reminder(slack_client, reminder_dict):
    # build interactive message
    message_attachment = [{
        "text": "Were you right?",
        "fallback": "Update Slack!",
        "callback_id": "prediction_" + str(reminder_dict["prediction_id"]),
        "color": "#3AA3E3",
        "attachment_type": "default",
        "actions": [
            {
                "name": "prediction_yes",
                "text": "Yes",
                "type": "button",
                "value": "true"
            },
            {
                "name": "prediction_no",
                "text": "No",
                "type": "button",
                "value": "false"
            }
        ]
    }]

    # send the message
    slack_client.api_call(
        "chat.postMessage",
        channel = reminder_dict["slack_id"],
        text = "You predicted that " +reminder_dict["description"],
        attachments = message_attachment
        )

def get_reminders(secret_key):
    # return a list of reminders using the API views we wrote
    headers = {"Secret-Key": secret_key}
    url = "https://d8c00abf.ngrok.io/predictions/api/predictions_for_notification"
    r = requests.get(url, headers = headers)
    return(eval(r.text))

slack_token = os.environ["SLACK_TOKEN"]
sc = SlackClient(slack_token)
reminders = get_reminders(os.environ['SECRET_KEY'])

for reminder in reminders:
    send_reminder(sc, reminder)
