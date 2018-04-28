from django.conf.urls import url

from . import views

urlpatterns = [
    url('test', views.test_slack_json),
    url('slack/message_action', views.slack_message_action),
    url('api/predictions_for_notification', views.api_predictions_for_notification)
]
