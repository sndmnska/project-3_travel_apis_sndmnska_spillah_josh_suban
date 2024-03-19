# To-do import module entries.
from api_travel_advisory import get_travel_advisory
from api_geolocation import geo_request
from api_geolocation import get_country_code
from db_handler import DBHandler
from data_presenter import DataPresenter

"""
This is main section
"""
from ui import message, user_question
from data_presenter import print_businesses
from api_food_to_eat import get_restaurants_for_location

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

    location = f"{user_city}, {user_country_code}"
    restaurants = get_restaurants_for_location(location)

    if restaurants:
        for restaurant in restaurants:
            print_businesses(restaurant)
            # add_restaurant_data(restaurant)

            make_choice = user_question("Press Enter to continuous or 'q' to quit: ")
            if make_choice.lower() == 'q':
                message("Thanks, goodbye.")
                break
    else:
        message('No restaurants found in the given location.')


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
    db_handler = DBHandler('records_db.sqlite')

    db_handler.create_table()# creates table if it does not exist

#the following lines add data using dbhandler methods

db_handler.add_travel_advisory(advisory_data)
db_handler.addd_food_to_eat(food_data)
db_handler.add_things_to_do(things_to_do_data)
db_handler.add_geo_location(geo_location_data)

# finding geo location data
place_name = "place name"
geo_location = DataPresenter.get_geolocation_data(place_name)
print(geo_location)


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    store_data()
