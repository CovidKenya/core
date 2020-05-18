import json
from datetime import datetime, timedelta

import requests
from django.utils import timezone
from django.utils.text import slugify

from requests.exceptions import HTTPError

from cases.models import Visual, Country

from cases.services.get_country_data import parse_country_data, get_countries_with_provinces, get_countries_without_provinces


def bulk_insert_data(visuals):
    vis = []
    for v in visuals:
        name = v.country.name
        slug = slugify(name)
        country, created = Country.objects.get_or_create(name=name, slug=slug)
        vis.append(Visual(date=v.date, cases=v.cases, deaths=v.deaths, recovered=v.recovered, country=country))
    Visual.objects.bulk_create(vis)

def get_local_data(data):
    visuals = parse_country_data(get_countries_without_provinces(data))
    bulk_insert_data(visuals)

def get_yesterday_data():
    try:
        response = requests.get(
            'https://disease.sh/v2/historical?lastdays=1')
        visuals = parse_country_data(get_countries_without_provinces(json.loads(response.text)))
        bulk_insert_data(visuals)
    except HTTPError as error:
        # handle HTTP errors
        print(f'HTTP error occurred: {error}')
    except Exception as error:
        # handle any other error
        print(f'Error: {error}')

def get_historical_data():
    start_date = datetime(2020, 1, 22)  # The earliest date available on the API
    today = datetime.today()
    days = (today - start_date).days

    try:
        response = requests.get(
            f'https://disease.sh/v2/historical?lastdays={days}')
        visuals = parse_country_data(get_countries_without_provinces(json.loads(response.text)))
        bulk_insert_data(visuals)
    except HTTPError as error:
        # handle HTTP errors
        print(f'HTTP error occurred: {error}')
    except Exception as error:
        # handle any other error
        print(f'Error: {error}')

