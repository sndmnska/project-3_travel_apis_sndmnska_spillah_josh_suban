import requests
import os

# Grab key from env variables.
api_key = os.environ.get('API_KEY')

# raises an error if environment variable is not set
assert api_key is not None

def main():
    city = get_city()
    country_code = get_geo_data(city)

    if country_code is None:
        print(f'Unable to find {city}.')
        return

    params = {'countrycode': country_code}
    url = 'https://www.travel-advisory.info/api'
    data = handle_request(url, params)

    country_data = data['data'][country_code]
    country_advisory = country_data['advisory']

    # Let me know if the tabs are a good idea or not, to me it makes it feel like its more grouped.
    print(f'The advisory for {country_data['name']}:')
    print(f'\t {country_advisory['message']}')
    print(f'\t Last updated: {country_advisory['updated']} UTC')
    print(f'\t Source: {country_advisory['source']}')

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


def get_geo_data(city):
    '''
    Converts user inputted city into country code.
    :param city: User's City.
    :return:
    '''
    params = {'q': city, 'limit': '1', 'APPID': api_key}
    url = 'http://api.openweathermap.org/geo/1.0/direct'
    data = handle_request(url, params)

    if len(data) == 0 or data is None:
        return None

    try:
        return data[0]['country']
    except Exception as e:
        print(e)

def get_city():
    '''
    Gets city from user's input.
    '''
    city = input('Input your chosen city: ')

    if not city or len(city) == 0 or not isinstance(city, str):
        print("Input correct city please.")
        return get_city()

    return city.capitalize()

main()