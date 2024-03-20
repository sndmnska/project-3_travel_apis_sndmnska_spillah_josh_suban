# To-do import module entries.
from api_travel_advisory import get_travel_advisory
from api_geolocation import geo_request
from api_geolocation import get_country_code
from db_handler import DBHandler
from data_presenter import DataPresenter

from api_things_to_do import get_random_local_event

from ui import message, user_question
from data_presenter import print_businesses
from api_food_to_eat import get_restaurants_for_location

user_city = None
user_country_code = None
travel_advisory_message = None
chosen_restaurant = None

event_name = None
event_url = None

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

    event_name, event_url = get_random_local_event(user_city)

    print(event_name)
    print(event_url)

    location = f"{user_city}, {user_country_code}"
    restaurants = get_restaurants_for_location(location)

    if restaurants:
        for restaurant in restaurants:
            print_businesses(restaurant)
            chosen_restaurant = restaurant
            # add_restaurant_data(restaurant)

            make_choice = user_question("Press Enter to continuous or 'q' to quit: ")
            if make_choice.lower() == 'q':
                message("Thanks, goodbye.")
                break
    else:
        message('No restaurants found in the given location.')

    store_data()


def get_city():
    """
        Gets city from user's input.
        This is used across multiple modules and is critical information.
        """

    city = None

    while not city or len(city) == 0 or not isinstance(city, str):
        city = input('Input your chosen city: ')

    return city.capitalize()

def store_data():
    db_handler = DBHandler()

    save_id = db_handler.create_table()# creates table if it does not exist
    # the following lines add data using dbhandler methods

    db_handler.add_travel_advisory(save_id, user_country_code, travel_advisory_message)
    db_handler.add_food_to_eat(save_id, user_city,chosen_restaurant)
    db_handler.add_things_to_do(save_id, event_name, event_url)
    db_handler.add_geo_location(save_id, user_city)

main()