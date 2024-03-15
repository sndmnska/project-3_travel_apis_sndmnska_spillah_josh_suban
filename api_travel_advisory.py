from ui import message
from api_geolocation import geo_request
from api_geolocation import get_country_code
from api_handler import handle_request


def main(city=''):
    if not city or len(city) == 0:
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

    # Let me know if the tabs are a good idea or not, to me, it makes it feel like its more grouped.
    message(f'The advisory for {country_data["name"]}:')
    message(f'\t {country_advisory["message"]}')
    message(f'\t Last updated: {country_advisory["updated"]} UTC')
    message(f'\t Source: {country_advisory["source"]}')

    return country_advisory["message"]


def parse_country_data(data, country_code):
    country_data = data['data'][country_code]
    country_advisory = country_data['advisory']

    return country_data, country_advisory


def get_city():  # To be replaced.
    """
    Gets city from user's input.
    """

    city = None

    while not city or len(city) == 0 or not isinstance(city, str):
        city = input('Input your chosen city: ')

    return city.capitalize()


main()
