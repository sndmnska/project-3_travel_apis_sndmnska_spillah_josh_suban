"""
Data Presenter: 

This module is used to process inputs from API calls and return the data in a user friendly format

"""
from ui import message
from db_handler import add_restaurant_data


# This is the data for the YELP API for the food to ear shows the data

def print_businesses(restaurant):
    if restaurant:
        name = restaurant.get('name')
        city = restaurant['location'].get('city')
        country = restaurant['location'].get('country')
        address = restaurant['location'].get('address1')
        message(f"Name: {name}, City: {city}, Country: {country}, Address: {address}")

        add_restaurant_data(name, city, country, address)

    else:
        message('No restaurants found in the given location.')

