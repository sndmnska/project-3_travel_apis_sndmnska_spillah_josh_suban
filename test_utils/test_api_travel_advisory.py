import unittest
from unittest import TestCase
from unittest.mock import patch, call, Mock
from api_travel_advisory import get_travel_advisory
from api_travel_advisory import parse_country_data

class TestTravelAdvisory(TestCase):

    def test_get_travel_advisory(self):
        country = "GB"
        results = get_travel_advisory(country_code)

        self.assertNotEqual(results, None)
        self.assertTrue(results.startswith("United Kingdom"))

    def test_parse_country_date(self):

        data = {'api_status': {'request': {'item': 'gb'}, 'reply': {'cache': 'cached', 'code': 200, 'status': 'ok', 'note': 'The api works, we could match requested country code.', 'count': 1}}, 'data': {'GB': {'iso_alpha2': 'GB', 'name': 'United Kingdom', 'continent': 'EU', 'advisory': {'score': 3, 'sources_active': 7, 'message': 'United Kingdom has a current risk level of 3 (out of 5). We advise: Use some caution when travelling United Kingdom.', 'updated': '2024-03-18 07:26:14', 'source': 'https://www.travel-advisory.info/united-kingdom'}}}}
        country_code = "GB"
        result = parse_country_data(data, country_code)

        expected_result = ({'iso_alpha2': 'GB', 'name': 'United Kingdom', 'continent': 'EU', 'advisory': {'score': 3, 'sources_active': 7, 'message': 'United Kingdom has a current risk level of 3 (out of 5). We advise: Use some caution when travelling United Kingdom.', 'updated': '2024-03-18 07:26:14', 'source': 'https://www.travel-advisory.info/united-kingdom'}}, {'score': 3, 'sources_active': 7, 'message': 'United Kingdom has a current risk level of 3 (out of 5). We advise: Use some caution when travelling United Kingdom.', 'updated': '2024-03-18 07:26:14', 'source': 'https://www.travel-advisory.info/united-kingdom'})

        self.assertEqual(result, expected_result)
