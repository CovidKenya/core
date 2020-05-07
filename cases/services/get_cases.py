import json
from datetime import datetime, timedelta

import requests
from requests.exceptions import HTTPError

from cases.models import Visual
from cases.services.clean_data import remove_provinces


def get_historical_data():
    start_date = datetime(2020, 1, 22)  # The earliest date available on the API
    today = datetime.today()
    days = (today - start_date).days

    try:
        response = requests.get(
            f'https://disease.sh/v2/historical?lastdays={days}')
    except HTTPError as error:
        # handle HTTP errors
        print(f'HTTP error occurred: {error}')
    except Exception as error:
        # handle any other error
        print(f'Error: {error}')
    else:
        # code is executed only if no exceptions were raised in the try block
        # generate a list of the days with data
        day_list = []
        while start_date + timedelta(days=1) < today:
            day_list.append(start_date.strftime("%-m/%-d/%y"))
            start_date += timedelta(days=1)

        # remove provinces
        filtered_data = remove_provinces(
            data=json.loads(response.text), date_range=day_list)

        #
        # save the data
        obj_list = []
        for i in filtered_data:
            obj_list.append(
                Visual(
                    country=i['country'],
                    case=i['timeline']['cases'],
                    recovery=i['timeline']['recovered'],
                    death=i['timeline']['deaths']
                ))

        # save all the objects in one query
        Visual.objects.bulk_create(obj_list)

        return filtered_data
