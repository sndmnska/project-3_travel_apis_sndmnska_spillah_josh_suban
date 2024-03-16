# To-do import module entries.
from api_travel_advisory import get_travel_advisory
from api_geolocation import geo_request
from api_geolocation import get_country_code

"""
Project 3 - A Useful Travel App (working title)


"""
user_city = None
user_country_code = None

travel_advisory_message = None

def main():
    """
    Main entry point for our program. Everything starts here.
    :return:
    """
    user_city = get_city()

    geo_data = geo_request(user_city)
    user_country_code = get_country_code(geo_data)

    # Put module entry points UNDER this.

    travel_advisory_message = get_travel_advisory(user_country_code)

def get_city():
    """
        Gets city from user's input.
        This is used across multiple modules and is critical information.
        """

    city = None

    while not city or len(city) == 0 or not isinstance(city, str):
        city = input('Input your chosen city: ')

    return city.capitalize()


main()
