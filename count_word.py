import datetime
import requests
import re


def count_word():
    input_word = 'systemutvecklare'

    today = datetime.datetime.now()
    week_ago = (today - datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%S")

    URL = "https://jobstream.api.jobtechdev.se/stream"
    PARAMS = {'date': week_ago}
    headers = {'api-key': 'developer', }

    responses = requests.get(url=URL, params=PARAMS, headers=headers)
    response_json = responses.json()

    response_list = [re.split(r'[^A-Öa-ö0-9]+', item['headline']) for item in response_json if item.get('headline', None)]

    count = 0

    for item_list in response_list:
        item_list_lower = [item.lower() for item in item_list]
        if input_word.lower() in item_list_lower:
            count = count + 1

    return count