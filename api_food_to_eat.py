
from ui import message
from api_handler import API_request
import os

# Yelp URL for the business search endpoint
url = 'https://api.yelp.com/v3/businesses/search'
key = os.environ.get('YELP_API_KEY')
headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {key}'
    }

def get_restaurants_for_location(location):

    # call function(s) that make API call
    # return data about restaurants
    params = {'term': 'Restaurants', 'location': location}

    response = API_request(url, headers=headers, params=params)

    if response is None:
        message(f"Failed to make API request for {location}")
        return None

    if 'businesses' not in response:
        return None

    restaurants = response['businesses']

    if not restaurants:
        message(f"No restaurants fount in this location: {location}")
    else:
        return restaurants

    #for restaurant in restaurants:
    #    return restaurant

    def convert_restaurant_name_to_str(restaurant):
        '''
        :input: [dict]  restaurant info
        :output: [str] restaurant name
        '''
        restaurant_name = restaurant['name']
        return restaurant_name

