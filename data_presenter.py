"""
Data Presenter: 

This module is used to process inputs from API calls and return the data in a user friendly format

"""

import sqlite3
from ui import message
from db_handler import add_restaurant_data

class DataPresenter:

    @staticmethod
    def add_bookmarks(user_id, place_name):

        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO bookmarks (user_id, place_name) VALUES (?, ?)", (user_id, place_name))

    @staticmethod
    def get_bookmarks(user_id):
        with sqlite3.connect('records_db.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT place_name FROM bookmarks WHERE user_id = ?", (user_id,))
            bookmarks = cursor.fetchall()
            if bookmarks:
                return [bookmark[0] for bookmark in bookmarks]
            else:
                return f"No bookmarks available for user ID {user_id}"
    @staticmethod
    def get_geolocation_data(place_name):
        with sqlite3.connect('records_db.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT latitude, longitude FROM geo_location WHERE place_name = ?", (place_name,))
            geo_data = cursor.fetchone()
            if geo_data:
                return f"Geo-location data for {place_name}: Latitude - {geo_data[0]}, Longitude - {geo_data[1]}"
            else:
                return f"Geo-location data for {place_name} not found in db"

    @staticmethod
    def add_food_to_eat(save_id,city, restaurant_name):
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO food_to_eat (save_id, city, restaurant_name) VALUES (?, ?, ?)",(save_id,city, restaurant_name))

    @staticmethod
    def add_things_to_do(save_id, event_title, event_url):
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO things_to_do (save_id, event_title, event_url) VALUES (?, ?, ?)", (save_id, event_title, event_url))


    @staticmethod
    def add_travel_advisory(save_id,country, advisory):
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO travel_advisory (save_id,country, advisory) VALUES (?, ?, ?)", (save_id, country, advisory))



    @staticmethod
    def handle_api_failure(place_name):
        # Handles API issues
        geo_data = DataPresenter.get_geolocation_data(place_name)
        return f"API for {place_name} not found. {geo_data}"




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


