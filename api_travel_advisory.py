import requests
import os
from ui import message

# Grab key from env variables.
geo_api_key = os.environ.get('GEO_API')

# raises an error if environment variable is not set
assert geo_api_key is not None

def main():
    city = get_city()
    geo_data = geo_request(city)

    if geo_data is None:
        message(f'Unable to find {city}.')
        return

    country_code = get_country_code(geo_data)

    if country_code is None:
        message(f'Unable to find {city}.')
        return

    params = {'countrycode': country_code}
    url = 'https://www.travel-advisory.info/api'
    data = handle_request(url, params)

    (country_data, country_advisory) = parse_country_data(data, country_code)

    # Let me know if the tabs are a good idea or not, to me it makes it feel like its more grouped.
    message(f'The advisory for {country_data["name"]}:')
    message(f'\t {country_advisory["message"]}')
    message(f'\t Last updated: {country_advisory["updated"]} UTC')
    message(f'\t Source: {country_advisory["source"]}')

    return data

def parse_country_data(data, country_code):
    country_data = data['data'][country_code]
    country_advisory = country_data['advisory']

    return country_data, country_advisory

def handle_request(url, params):
    '''
    Manages error handling for our requests.
    :param url: API URL
    :param params: API parameters
    :return: json if successful or None if not.
    '''
    response = requests.get(url, params)

    if response.status_code == 200:
        return response.json()
    if response.status_code == 404:
        return None


def geo_request(city):
    '''
    Converts user inputted city into country code.
    :param city: User's City.
    :return: Dict of user's geo request or None if not found.
    '''
    params = {'q': city, 'limit': '1', 'APPID': geo_api_key}
    url = 'http://api.openweathermap.org/geo/1.0/direct'
    data = None

    try:
        data = handle_request(url, params)
    except requests.exceptions.ConnectionError as e:
        message('Please check your internet connection!')
        return None
    except Exception:
        message('An Unknown error has occurred!')
        return None

    if not data or len(data) == 0:
        return None
    else:
        return data


def get_country_code(data):
    '''
    :param data: Dict of user's chosen city geo data.
    :return: String of ISO-2 country code or None if invalid.
    '''

    if not data or len(data) == 0 or not data[0] or not data[0]['country']:
        return None

    return data[0]['country']

def get_city():
    '''
    Gets city from user's input.
    '''

    city = None

    while not city or len(city) == 0 or not isinstance(city, str):
        city = input('Input your chosen city: ')

    return city.capitalize()

main()