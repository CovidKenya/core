# from django.test import TestCase
from unittest import TestCase

from cases.services.get_country_data import (parse_date, parse_country_data,
                                             get_countries_without_provinces,
                                             get_countries_with_provinces,
                                             merge_reduce_countries)

from cases.services.data import data

class TestJSONDataParser(TestCase):
    def setUp(self):
        self.data = data

    def test_parse_date(self):
        date_string = '5/13/20'
        date_obj = parse_date(date_string)
        self.assertEqual(date_obj.year, 2020)
        self.assertEqual(date_obj.month, 5)
        self.assertEqual(date_obj.day, 13)

    def test_parse_date_raises_value_error_if_format_is_wrong(self):
        with self.assertRaises(ValueError):
            parse_date('s-d-5')

        with self.assertRaises(ValueError):
            parse_date('5-13-20')

        with self.assertRaises(ValueError):
            parse_date('2.21.17')

    def test_get_countries_with_provinces(self):
        countries = get_countries_with_provinces(data)
        self.assertEqual(81, len(countries))

    def test_get_countries_with_provinces_raises_value_error_if_data_is_none(self):
        with self.assertRaises(ValueError):
            get_countries_with_provinces(None)

    def test_get_countries_with_provinces_raises_value_error_if_data_is_empty(self):
        with self.assertRaises(ValueError):
            get_countries_with_provinces([])

    def test_get_countries_without_provinces(self):
        countries = get_countries_without_provinces(data)
        self.assertEqual(185, len(countries))

    def test_get_countries_without_provinces_raises_value_error_if_data_is_none(self):
        with self.assertRaises(ValueError):
            get_countries_without_provinces(None)

    def test_get_countries_without_provinces_paises_value_error_if_data_is_empty(self):
        with self.assertRaises(ValueError):
            get_countries_without_provinces([])

    def test_merge_reduce_countries(self):
        countries_w_p = get_countries_with_provinces(data)
        countries_wout_p = get_countries_without_provinces(data)
        countries_merged = merge_reduce_countries(countries_w_p, countries_wout_p)
        self.assertEqual(len(countries_merged), 266)

if __name__ == '__main__':
    unittest.main()
