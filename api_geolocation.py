from api_handler import API_request
import os

# Grab key from env variables.
api_key = os.environ.get('GEO_API')

# raises an error if environment variable is not set
assert api_key is not None

def geo_request(city):
    '''
    Converts user inputted city into country code.
    :param city: User's City.
    :return: Dict of user's geo request or None if not found.
    '''
    params = {'q': city, 'limit': '1', 'APPID': api_key}
    url = 'http://api.openweathermap.org/geo/1.0/direct'

    data = API_request(url, params)

    if not data or len(data) == 0:
        return None
    else:
        return data