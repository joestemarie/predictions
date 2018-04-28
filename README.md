# predictions
This app uses Slack to track predictions made over time and measure how well I predict different events. It will also include reflection questions to prompt me to think about what information I wish I'd had.

The basic flow looks like this:
![preview of flow](https://www.dropbox.com/s/ge69c5tsfxmww7u/Screenshot%202018-04-28%2012.46.26.png?dl=0&raw=1 "Text")

The app runs on Django (one day, I'll build a web app interface to build dashboards with) and Slack.

## Background Tasks
Rather than building a background task server, we use AWS Lambda and CloudWatch to trigger follow-ups on predictions. Every 10 minutes, AWS CloudWatch triggers Lambda to go search for all outstanding predictions and run them.
