"""
This is main section
"""
from ui import message
from data_presenter import print_businesses
from api_food_to_eat import get_restaurants_for_location


def main():

    city = input('Enter the name of the city: ').strip()
    country = input('Enter the 2-letter country code: ').strip().upper()

    location = f"{city}, {country}"
    restaurants = get_restaurants_for_location(location)

    if restaurants:
        for restaurant in restaurants:
            print_businesses(restaurant)
            # add_restaurant_data(restaurant)

            make_choice = input("Press Enter to continuous or 'q' to quit: ")
            if make_choice.lower() == 'q':
                message("Thanks, goodbye.")
                break
    else:
        message('No restaurants found in the given location.')


"""