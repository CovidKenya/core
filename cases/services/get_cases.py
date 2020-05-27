import json
from datetime import datetime, timedelta

import requests
from requests.exceptions import HTTPError

from cases.models import VisualCases
from cases.services.clean_data import remove_provinces
from cases.services.save_visuals_data import save_historical_data


def get_start_date():
    try:
        return VisualCases.objects.latest("date").date
    except VisualCases.DoesNotExist:
        return datetime(2020, 1, 22).date()  # The earliest date available on the API


def get_historical_data():
    start_date = get_start_date()
    earliest_data_available = datetime.utcnow().date() - timedelta(days=1)

    days = (earliest_data_available - start_date).days

    if days < 1:
        return

    try:
        response = requests.get(
            f'https://disease.sh/v2/historical?lastdays={days}')
        day_list = []
        start_date += timedelta(days=1)
        while start_date < earliest_data_available:
            day_list.append(start_date.strftime("%-m/%-d/%y"))
            start_date += timedelta(days=1)

        # remove provinces
        filtered_data = remove_provinces(
            data=json.loads(response.text), date_range=day_list)

        # save the data
        save_historical_data(filtered_data)

    except HTTPError:
        # handle HTTP errors
        raise Exception("Network Error")
    except Exception as error:
        # handle any other error
        raise error
    else:
        return True
