import unittest
from unittest import TestCase
from unittest.mock import patch, call, Mock
from api_geolocation import geo_request
from api_geolocation import get_country_code

class TestAPIGeo(TestCase):

    def test_geo_request(self):
        city = "London"
        results = geo_request(city)

        self.assertNotEqual(results, None)
        self.assertEqual(results[0]['name'], city)
        self.assertEqual(results[0]['country'], "GB")
        self.assertEqual(results[0]['state'], "England")

    def test_get_country_code(self):

        data = [{'name': 'London', 'local_names': {'se': 'London', 'gn': 'Lóndyre', 'ky': 'Лондон', 'fo': 'London', 'fj': 'Lodoni', 'bs': 'London', 'bn': 'লন্ডন', 'nl': 'Londen', 'he': 'לונדון', 'sv': 'London', 'fy': 'Londen', 'af': 'Londen', 'ay': 'London', 'en': 'London', 'ce': 'Лондон', 'ca': 'Londres', 'uz': 'London', 'lo': 'ລອນດອນ', 'da': 'London', 'tk': 'London', 'ku': 'London', 'ab': 'Лондон', 'pt': 'Londres', 'hy': 'Լոնդոն', 'to': 'Lonitoni', 'gu': 'લંડન', 'kk': 'Лондон', 'st': 'London', 'my': 'လန်ဒန်မြို့', 'ka': 'ლონდონი', 'ru': 'Лондон', 'tg': 'Лондон', 'et': 'London', 'pa': 'ਲੰਡਨ', 'om': 'Landan', 'ny': 'London', 'te': 'లండన్', 'hi': 'लंदन', 'an': 'Londres', 'kw': 'Loundres', 'os': 'Лондон', 'pl': 'Londyn', 'sw': 'London', 'mg': 'Lôndôna', 'cy': 'Llundain', 'nn': 'London', 'so': 'London', 'gd': 'Lunnainn', 'ms': 'London', 'ee': 'London', 'gl': 'Londres', 'mk': 'Лондон', 'bi': 'London', 'na': 'London', 'li': 'Londe', 'ba': 'Лондон', 'vo': 'London', 'wo': 'Londar', 'is': 'London', 'ne': 'लन्डन', 'kv': 'Лондон', 'ie': 'London', 'jv': 'London', 'mn': 'Лондон', 'uk': 'Лондон', 'si': 'ලන්ඩන්', 'feature_name': 'London', 'hr': 'London', 'th': 'ลอนดอน', 'ascii': 'London', 'wa': 'Londe', 'cv': 'Лондон', 'nv': 'Tooh Dineʼé Bikin Haalʼá', 'mt': 'Londra', 'av': 'Лондон', 'oc': 'Londres', 'bm': 'London', 'lv': 'Londona', 'be': 'Лондан', 'yi': 'לאנדאן', 'kl': 'London', 'br': 'Londrez', 'or': 'ଲଣ୍ଡନ', 'ps': 'لندن', 'bg': 'Лондон', 'ur': 'علاقہ لندن', 'bh': 'लंदन', 'qu': 'London', 'sh': 'London', 'lb': 'London', 'zh': '伦敦', 'sn': 'London', 'fi': 'Lontoo', 'hu': 'London', 'ha': 'Landan', 'es': 'Londres', 'co': 'Londra', 'tw': 'London', 'eo': 'Londono', 'id': 'London', 'no': 'London', 'tl': 'Londres', 'cu': 'Лондонъ', 'ln': 'Lóndɛlɛ', 'ml': 'ലണ്ടൻ', 'ro': 'Londra', 'sr': 'Лондон', 'ja': 'ロンドン', 'el': 'Λονδίνο', 'tr': 'Londra', 'bo': 'ལོན་ཊོན།', 'fr': 'Londres', 'vi': 'Luân Đôn', 'su': 'London', 'ko': '런던', 'fa': 'لندن', 'ig': 'London', 'gv': 'Lunnin', 'it': 'Londra', 'de': 'London', 'ga': 'Londain', 'sk': 'Londýn', 'ht': 'Lonn', 'cs': 'Londýn', 'lt': 'Londonas', 'ar': 'لندن', 'ug': 'لوندۇن', 'eu': 'Londres', 'tt': 'Лондон', 'mi': 'Rānana', 'az': 'London', 'sa': 'लन्डन्', 'am': 'ለንደን', 'mr': 'लंडन', 'ia': 'London', 'km': 'ឡុងដ៍', 'sc': 'Londra', 'zu': 'ILondon', 'ta': 'இலண்டன்', 'yo': 'Lọndọnu', 'io': 'London', 'sl': 'London', 'sm': 'Lonetona', 'kn': 'ಲಂಡನ್', 'ff': 'London', 'sq': 'Londra', 'sd': 'لنڊن', 'rm': 'Londra'}, 'lat': 51.5073219, 'lon': -0.1276474, 'country': 'GB', 'state': 'England'}]
        expected_country_code = "GB"
        result = get_country_code(data)

        self.assertEqual(result, expected_country_code)