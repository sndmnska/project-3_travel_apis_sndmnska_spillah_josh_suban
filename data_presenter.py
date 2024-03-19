"""
Data Presenter: 

This module is used to process inputs from API calls and return the data in a user friendly format

"""
import sqlite3

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
    def add_food_to_eat(city, food_name, description):
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO foods_to_eat (city, food_name, description) VALUES (?, ?, ?)",(city, food_name, description))

    @staticmethod
    def add_things_to_do(place_name, activity, description):
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO things_to_do (place_name, activity, description) VALUES (?, ?, ?)", (place_name, activity, description))


    @staticmethod
    def add_travel_advisory(country, advisory):
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO travel_advisory (country, advisory) VALUES (?, ?)", (country, advisory))



    @staticmethod
    def handle_api_failure(place_name):
        # Handles API issues
        geo_data = DataPresenter.get_geolocation_data(place_name)
        return f"API for {place_name} not found. {geo_data}"