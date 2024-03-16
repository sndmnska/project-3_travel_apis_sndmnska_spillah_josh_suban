"""
DB Handler

This module communicates between the main.py program and the SQLite database
"""
import sqlite3

def create_table():
    # Create table if is not exists
    with sqlite3.connect('records_db.sqlite') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS restaurants (name TEXT, city TEXT, country TEXT, address TEXT)')
    conn.close()


def add_restaurant_data(name, city, country, address):

    create_table()

    with sqlite3.connect('records_db.sqlite') as conn:
        conn.execute("INSERT INTO restaurants VALUES (?, ?, ?, ?)", (name, city, country, address))
    conn.close()

