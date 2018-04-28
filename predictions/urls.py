from django.conf.urls import url

from . import views

urlpatterns = [
    url('test', views.test_slack_json),
    url('api/predictions_for_notification', views.api_predictions_for_notification)
]
