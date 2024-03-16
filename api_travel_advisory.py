from ui import message
from api_handler import handle_request


def get_travel_advisory(user_country_code):
    if not user_country_code or len(user_country_code) == 0:
        message("Error: Missing User Country Code!")
        return None

    params = {'countrycode': user_country_code}
    url = 'https://www.travel-advisory.info/api'
    data = handle_request(url, None, params)

    (country_data, country_advisory) = parse_country_data(data, user_country_code)

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
