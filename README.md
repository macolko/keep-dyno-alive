# Lambda Woke Dyno

The repository contains a tiny lambda function (deployed as a Docker container) that sends a request to the specified URLs every 20 minutes, Monday to Friday.

You can specify URLs to send requests to in the environment variable `heroku_apps`, separated by a comma.

Additionally, you can specify starting and ending hour (in UTC).

    start_hour=9
    end_hour=17

Requests will not be made with the lambda execution occurs outside the specified hours. It is useful to simplify setting cron job (where you can specify execution every 20 minutes, Monday to Friday but would like to run the pinger only on specific hours of the day).

### Scheduling

Lambda can be scheduled to run with `CloudWatch` events. Currently, it is scheduled to run every 20 minutes, Monday to Friday:

    0/20 * ? * MON-FRI *