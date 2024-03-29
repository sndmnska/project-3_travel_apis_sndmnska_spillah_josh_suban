"""
DB Handler

This module communicates between the main.py program and the SQLite database to process and display data in a user frienly manner
"""
import sqlite3

class DBHandler:
    def create_table(self):  # to check if table exists
        # creates table if table does not exists

        save_id = 0
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute(
                'CREATE TABLE IF NOT EXISTS food_to_eat(id INTEGER, city TEXT, restaurant_name TEXT)')

            conn.execute('CREATE TABLE IF NOT EXISTS travel_advisory(id INTEGER, country TEXT, advisory TEXT)')
            conn.execute('CREATE TABLE IF NOT EXISTS things_to_do(id INTEGER, title TEXT, url TEXT)')
            conn.execute(
                'CREATE TABLE IF NOT EXISTS geo_location(id INTEGER, place_name TEXT)')
            cursor = conn.cursor()
            cursor.execute("SELECT count(country) FROM travel_advisory")
            (data_test, ) = cursor.fetchone()

            save_id = data_test + save_id

        conn.close()

        return save_id

    # functions to put data in the right tables in the SQLITE database

    def add_food_to_eat(self, save_id, city, restaurant_name):

        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO food_to_eat VALUES (?,?,?)", (save_id, city, restaurant_name))
        conn.close()

    def add_travel_advisory(self, save_id, country, advisory):

        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO travel_advisory VALUES (?,?,?)", (save_id, country, advisory))  # Country code
        conn.close()

    def add_things_to_do(self, save_id, event_title, event_url):

        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO things_to_do VALUES (?,?,?)", (save_id, event_title, event_url))

        conn.close()

    def add_geo_location(self, save_id, place_name):

        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO geo_location VALUES (?,?)", (save_id, place_name))
        conn.close()


