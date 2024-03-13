from pprint import pprint

import requests
import os

# Yelp URL for the business search endpoint
url = 'https://api.yelp.com/v3/businesses/search'
key = os.environ.get('YELP_API_KEY')


def main():  # Main function for the program
    location = get_location() # Gets the user location input
    response, error = make_api_request(location, key)  # Handle exceptions in program

    if error:
        print(error)
        print('Sorry, Somthing went wrong')
        return

    if response: # this is the response of the program
        restaurant_address = get_restaurant_from_api_response(response)
        if restaurant_address:
            print_businesses(restaurant_address)
        else:
            print('No location found.')


def get_location(): # This function gets the location for user
    city, country = '', ''
    while len(city) == 0:
        city = input('Enter the name of the city: ').strip()

    while len(country) != 2 or not country.isalpha():
        country = input('Enter the 2-letter country code: ').strip()

    location = f'{city}, {country}'  # This is formation of the location
    return location

# This is the functions to request data from YELP API
def make_api_request(location, key):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {key}'
        }
        # This founds runts that is in the location user input
        params = {'term': 'Restaurants', 'location': location}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise exception
        data = response.json()   # this may error too, if response is not JSON
        return data, None
    except requests.RequestException as e:
        return None, f"Error making API request: {e}"


# this function gets the restaurant information from the yelp API
def get_restaurant_from_api_response(response):
    businesses = response.get('businesses', [])
    return businesses


# Gets each restaurant from the data
def print_businesses(businesses):
    for restaurant in businesses:
        name = restaurant.get('name')
        city = restaurant['location'].get('city')
        country = restaurant['location'].get('country')
        address = restaurant['location'].get('address1')
        print(f"Name: {name}, City: {city}, Country: {country}, Address: {address}")


if __name__ == "__main__":
    main()

