"""Get Country Data module exposes
classes: Country, Visual
functions: parse_data, parse_country_data,
    get_countries_with_provinces,
    get_countries_without_provinces,

"""
from datetime import date
import re

class Country():
    """Takes a name: string and creates
    an object mimicking the:
    cases,models.Country model.
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Visual():
    """Takes a date_object: datetime.date
    and a tuple containing the values for:
    cases: int, deaths: int, recovered: int
    and country: Country object and creates
    an object mimicking the:
    cases.models.Visula model.
    """
    def __init__(self, date_object, args):
        self.date = date_object
        self.cases = args[0]
        self.deaths = args[1]
        self.recovered = args[2]
        self.country = args[3]

    def __str__(self):
        return f'Visual {self.country.name}'

    def __repr__(self):
        return f'Visual {self.country.name}'

def parse_date(date_string):
    """Takes a date_string: string in the format 'm/d/y'
    and extracts the month, day and year respectively.
    Returns a datetime.date object constructed using
    the month, day and year values.
    """
    date_tuple = re.match(r"(\d+)/(\d+)/(\d+)", date_string)
    if not date_tuple:
        raise ValueError("Invalid pattern: required format: 'm/d/y' ")
    (month, day, year) = date_tuple.group().split('/')
    return date(int('20' + year), int(month), int(day))

def get_countries_with_provinces(data):
    """Takes one list argument of dictionaries
    and parses it for:
    hint: date_to_num = dict(date: string = count: int)
    country: string
    cases: list(date_to_num)
    deaths: list(date_to_num)
    recovered: list(date_to_num)
    Returns a list of tuples containing dictionaries of
    countries which HAVE provinces NOT None and their
    related dictionaries of:
    cases, deaths and recovered
    """
    if not data or data == []:
        raise ValueError('data list cannot be empty or None')

    return list(filter(lambda x: x['province'] is not None, data))

def get_countries_without_provinces(data):
    """Takes one list argument of dictionaries
    and parses it for:
    hint: date_to_num = dict(date: string = count: int)
    country: string
    cases: list(date_to_num)
    deaths: list(date_to_num)
    recovered: list(date_to_num)
    Returns a list of tuples containing dictionaries
    of countries which HAVE provinces == None and its
    with their related dictionaries of:
    cases, deaths and recovered
    """
    if not data or data == []:
        raise ValueError('data list cannot be empty')

    return list(filter(lambda x: x['province'] is None, data))

def merge_reduce_countries(countries_w_p, countries_wout_p):
    """Takes two lists arguments of tuples containig
    covid-19 country data dictionaries.
    Then it iterartes the countries_w_p: list(tuple)
    and groups them based on country before it checks
    to see if that country exists in countries_wout_p.
    1. If it is there it SUMS up subsequent fields:
    cases, deaths and recovered of contries_wp BEFORE
    it further SUMS up with the existing country_wout_p
    of the same country field.
    2. Else it just computes step 1 above and appends
    the country_wp tuple into the list of countries_wout_p.
    """
    for country in countries_w_p:
        # country['country'] = str.upper(country['province'][0]) + country['province'][1:]
        country['country'] = country['country'] + ', ' + country['province']

    for country in countries_w_p:
        countries_wout_p.append(country)

    return list(map(lambda x: (
                {'country': x['country']},
                {'cases': x['timeline']['cases']},
                {'deaths': x['timeline']['deaths']},
                {'recovered': x['timeline']['recovered']}
                ), countries_wout_p))

def parse_country_data(data):
    """ Takes one list of tuple arguments containing
    covid-19 country data dictionaries.
    hint: date_to_num = dict(date: string = count: int)
    key: 'country', value: string
    key: 'cases', value: list(date_to_num),
    key: 'deaths', value: list(date_to_num)
    key: 'recovered', value: list(date_to_num)
    Returns list of Visual objects
    """
    if not data or data == []:
        raise ValueError('data list cannot be empty')

    data = list(map(lambda x: (
                {'country': x['country']},
                {'cases': x['timeline']['cases']},
                {'deaths': x['timeline']['deaths']},
                {'recovered': x['timeline']['recovered']}
                ), data))

    visuals = []
    for item in data:
        country = Country(name=item[0]['country'])
        for (date_string, _) in item[1]['cases'].items():
            objs = (item[1]['cases'][date_string],
                    item[2]['deaths'][date_string],
                    item[3]['recovered'][date_string], country)
            visuals.append(Visual(parse_date(date_string), objs))
    return visuals
