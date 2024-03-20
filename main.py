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

def user_main_menu():

    menu = '''
    Please choose a menu option: 
    \t(1): Lookup Information for new city
    \t(2): Retrieve stored information
    \t(Q): Quit program

    Enter your choice: '''
    
    while True:
        menu_choice = user_question(menu)
        if menu_choice == '1' or menu_choice == '2' or menu_choice.upper() == "Q":
            return menu_choice
        else: 
            message("Please choose a valid menu option.")



def lookup_city_and_retrieve_travel_information():
    user_city = get_city()

    geo_data = geo_request(user_city)
    user_country_code = get_country_code(geo_data)

    # Put module entry points UNDER this.

    travel_advisory_message = get_travel_advisory(user_country_code)

    event_name, event_url = get_random_local_event(user_city)
    
    message(event_name)
    message(event_url)

    location = f"{user_city}, {user_country_code}"
    restaurants = get_restaurants_for_location(location)

    
    if restaurants:
        for restaurant in restaurants:
            print_businesses(restaurant)
            chosen_restaurant = restaurant
            # add_restaurant_data(restaurant)

            make_choice = user_question("If you want to lookup a different restaurant, press ENTER. Otherwise press 's' to SAVE your restaurant: ")
            if make_choice.lower() == 's' or make_choice.lower() == 'save':
                message("Restaurant chosen.")
                break
    else:
        message('No restaurants found in the given location.')
    
    save_bool = None
    while True:
        save_choice = user_question("Would you like to save this data in the database? Y/N: ")
        if save_choice.upper() == 'Y' or save_choice.upper == 'N':
            if save_choice.upper == 'Y':
                save_bool = True
            if save_choice.upper == 'N':
                save_bool = False
            break

    return save_bool 

def incomplete_feature():
    # HACK - This is just to get the menu working with something.  Displays a message saying feature not yet implimented.
    message('Our apologies: This feature is not yet implimented')

def main():
    """
    Main entry point for our program. Everything starts here.
    :return:
    """
    welcome_msg= '''**Welcome to your travel helper program!** 
    
    This program can look up any city and get information about any travel advisories.
    It also looks up a random event in that city from TicketMaster and displays a place where you can eat some tasty food.
    '''
    message(welcome_msg)
    while True:
        chosen_option = user_main_menu()
        if chosen_option == '1':
            save_to_db_boolean = lookup_city_and_retrieve_travel_information()
            if save_to_db_boolean is True:
                store_data()
        elif chosen_option == '2':
            incomplete_feature()
        elif chosen_option.upper() == 'Q':
            break
        else:
            message('Error, please try again.')

    






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