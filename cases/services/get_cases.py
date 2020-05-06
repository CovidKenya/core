import json
import requests
from requests.exceptions import HTTPError


def get_historical_data(days):
    try:
        response = requests.get(
            f'https://disease.sh/v2/historical?lastdays={days}')
    except HTTPError as error:
        print(f'HTTP error occurred: {error}')
    except Exception as error:
        print(f'Error: {error}')
    else:
        api_data = json.loads(response.text)
        for i in(api_data):
            print(i)

