"""
This is main section
"""
from ui import message
from api_food_to_eat import get_restaurants_for_location

def main():
    city = input('Enter the name of the city: ').strip()
    country = input('Enter the 2-letter country code: ').strip().upper()

    location = f"{city}, {country}"
    restaurants = get_restaurants_for_location(location)

    if restaurants:
        for restaurant in restaurants:
            name = restaurant.get('name')
            city = restaurant['location'].get('city')
            country = restaurant['location'].get('country')
            address = restaurant['location'].get('address1')
            message(f"Name: {name}, City: {city}, Country: {country}, Address: {address}")
    else:
        message('No restaurants found in the given location.')


if __name__ == "__main__":
    main()

