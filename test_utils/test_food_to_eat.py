import unittest
from unittest import TestCase
from unittest.mock import patch, call, Mock
from api_food_to_eat import get_restaurants_for_location

class TestFoodToEat(TestCase):
    @patch('requests.get')

    def test_get_restaurants_for_location(self, mock_requests_get):
        # what am I testing?  Testing for returning a tuple of (city, country) upon success.
        # It doesn't really matter what the 'response' contains, only that a tuple is returned if no Exception is thrown. 
        # arrange
        api_response_example = {
            'businesses': [
                {'name': 'Restaurant 1'},
                {'name': 'Restaurant 2'},
                {'name': 'Restaurant 3'}
            ]
        }

        # this to return a mock request
        mock_requests_get().json.return_value = api_response_example

        expected_location = "Minneapolis, US"
        restaurants = get_restaurants_for_location(expected_location)

        self.assertEqual(len(restaurants), 3)
        self.assertEqual(restaurants[0]['name'], 'Restaurant 1')
        self.assertEqual(restaurants[1]['name'], 'Restaurant 2')
        self.assertEqual(restaurants[2]['name'], 'Restaurant 3')
        

if __name__ == '__main__':
    unittest.main()
