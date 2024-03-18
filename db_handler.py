"""
DB Handler

This module communicates between the main.py program and the SQLite database to process and display data in a user frienly manner
"""
import sqlite3

def create_table(): # to check if table exists
    #creates table if table does not exists
    with sqlite3.connect('records_db.sqlite') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS restaurant_data(country TEXT, restaurant TEXT, description TEXT')

        conn.execute('CREATE TABLE IF NOT EXISTS food_to_eat(country TEXT, food_name TEXT, description TEXT')
        conn.execute('CREATE TABLE IF NOT EXISTS travel_advisory(country TEXT, advisory TEXT')
        conn.execute('CREATE TABLE IF NOT EXISTS things_to_do(place_name TEXT, activity TEXT, description TEXT ')
        conn.execute('CREATE TABLE IF NOT EXISTS geo_location(place_name TEXT, latitude TEXT, longtitude TEXT')
    conn.close()

# functions to put data in the right tables in the SQLITE database
    def add_restaurant_data(name, city, country, address):
        create_table()
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO restaurants VALUES (?, ?, ?, ?)", (name, city, country, address))
        conn.close()

    def add_food_to_eat(country, food_name,description):
        create_table
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO food_to_eat VALUES (?,?,?)", (country, food_name, description))
        conn.close()


    def add_travel_advisory( country, advisory):
        create_table()
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO travel_advisory VALUES (?,?,)", (country, advisory))
        conn.close()


    def add_things_to_do(place_name, activivty, description):
        create_table()
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO things_to_do VALUES (?,?,?)", (place_name, activivty,description))

        conn.close()



    def add_geo_location(place_name, latitude,longitude):
        create_table()
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO geo_location VALUES (?,?,?)", (place_name, latitude,longitude))
        conn.close()