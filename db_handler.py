"""
DB Handler

This module communicates between the main.py program and the SQLite database to process and display data in a user frienly manner
"""
import sqlite3

def create_table(): # to check if table exists
    #creates table if table does not exists
    with sqlite3.connect('records_db.sqlite') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS food_to_eat(id INTEGER, city TEXT, country TEXT, address TEXT, restaurant_name TEXT')
        conn.execute('CREATE TABLE IF NOT EXISTS travel_advisory(id INTEGER, country TEXT, advisory TEXT')
        conn.execute('CREATE TABLE IF NOT EXISTS things_to_do(id INTEGER, title TEXT, url TEXT, city TEXT')
        conn.execute('CREATE TABLE IF NOT EXISTS geo_location(id INTEGER, place_name TEXT, latitude TEXT, longtitude TEXT')
    conn.close()

# functions to put data in the right tables in the SQLITE database

    def add_food_to_eat(save_id, city, restaurant_name):
        create_table
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO food_to_eat VALUES (?,?,?)", (save_id, city, restaurant_name))
        conn.close()


    def add_travel_advisory(save_id, country, advisory):
        create_table()
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO travel_advisory VALUES (?,?,?)", (save_id, country, advisory)) # Country code
        conn.close()


    def add_things_to_do(save_id, event_title, event_url):
        create_table()
        with sqlite3.connect('records_db.sqlite') as conn:
            conn.execute("INSERT INTO things_to_do VALUES (?,?,?)", (save_id, event_title, event_url))

        conn.close()



    def add_geo_location(save_id, place_name, latitude,longitude):
        create_table()
        with sqlite3.connect('records_db.sqlite') as conn:

            conn.execute("INSERT INTO geo_location VALUES (?,?)", (save_id, place_name))
        conn.close()



# OLD CODE,
# 
# def create_table():
#     # Create table if is not exists
#     with sqlite3.connect('records_db.sqlite') as conn:
#         conn.execute('CREATE TABLE IF NOT EXISTS restaurants (name TEXT, city TEXT, city TEXT, address TEXT)')
#     conn.close()


# def add_restaurant_data(name, city, city, address):

#     create_table()

#     with sqlite3.connect('records_db.sqlite') as conn:
#         conn.execute("INSERT INTO restaurants VALUES (?, ?, ?, ?)", (name, city, city, address))
#     conn.close()


