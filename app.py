import requests
import os
from datetime import datetime


def handler(event, context):
    if not is_in_runtime_window():
        return

    urls = os.environ['heroku_apps']
    urls = [url.strip() for url in urls.split(',')]
    for url in urls:
        res = requests.get(url)
        print(f"Sent request to {url}")
        print(f"Response: {res}")
        res.raise_for_status()


def is_in_runtime_window() -> bool:
    # UTC start and end time (hour)
    start = os.environ.get('start_hour')
    end = os.environ.get('end_hour')
    if not start or not end:
        return True

    current = datetime.utcnow()
    if not int(start) <= current.hour <= int(end):
        print(f"Request out of window.")
        return False
    return True
