import requests
headers = {"Secret-Key": SECRET_KEY}
url = "https://d8c00abf.ngrok.io/predictions/api/predictions_for_notification"
r = requests.get(url, headers = headers)
