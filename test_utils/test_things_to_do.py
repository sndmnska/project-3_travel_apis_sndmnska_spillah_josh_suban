from api_things_to_do import get_random_event_from_response, convert_event_to_strings
from unittest import TestCase
from unittest.mock import patch, call, Mock

# Arrange, Act, Assert


# NOTE: Nested dictionaries not important to api_things_to_do module and this test module 
# are represented by: {"..."}

# There are 20 events in sample_ticketmaster_api_response
# All events contain the same dictionary ["(EXAMPLE_EVENT)"]
# In order to show the assertion that one of these instances was chosen.
sample_full_ticketmaster_api_response =   {
    '_embedded': { 'events': [
    {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, 
    {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, 
    {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, 
    {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}, {"(EXAMPLE_EVENT)"}]}, 
    '_links': {'first': {"..."}, 'self': {"..."}, 'next': {"..."}, 'last': {"..."}}, 
    'page': {'size': 20, 'totalElements': 897, 'totalPages': 45, 'number': 0}
    }

sample_single_event_ticketmaster_api_response = {
    'name': 'Minnesota Twins vs. Los Angeles Dodgers', 'type': 'event', 'id': 'Z7r9jZ1AdPbOp', 
    'test': False, 'url': 'https://www.ticketmaster.com/event/Z7r9jZ1AdPbOp', 'locale': 'en-us', 
    'images': [{"..."}, {"..."}, {"..."}, {"..."}, {"..."}, {"..."}, {"..."}, {"..."}, {"..."}, {"..."}], 
    'sales': {'public': {"..."}}, 'dates': {'start': {"..."}, 'status': {"..."}, 'spanMultipleDays': False}, 
    'classifications': [{"..."}], 'outlets': [{"..."}, {"..."}], 'seatmap': 
    {'staticUrl': 'https://content.resale.ticketmaster.com/graphics/TMResale/1/VenueMaps/6751-554-3-0-TargetFieldMinnesotaTwins.png'}, 
    'ticketing': {'allInclusivePricing': {"..."}}, '_links': {'self': {"..."}, 'attractions': ["..."], 'venues': ["..."]}, '_embedded': 
    {'venues': ["..."], 'attractions': ["..."]}
    }


class TestThingsToDo(TestCase):
    def test_get_random_event_from_response_expected_dict(self):
        sample_dict = sample_full_ticketmaster_api_response
        actual_response = get_random_event_from_response(sample_dict)
        expected_response = {"(EXAMPLE_EVENT)"}
        self.assertEqual(expected_response, actual_response)


    def test_get_random_event_from_response_return_None_on_KeyError(self):
        incorrect_dict = {'foo':[{'bar': 'baz'}, {'not':'a'}], 'real': 'response'}
        actual_response = get_random_event_from_response(incorrect_dict)
        self.assertEqual(actual_response, None)

    def test_convert_event_to_strings_expected_dict(self):
        sample_event = sample_single_event_ticketmaster_api_response
        actual_name, actual_url = convert_event_to_strings(sample_event)
        expected_name = 'Minnesota Twins vs. Los Angeles Dodgers'
        expected_url = 'https://www.ticketmaster.com/event/Z7r9jZ1AdPbOp'
        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected_url, actual_url)

    def test_convert_event_to_strings_return_None_tuple_on_KeyError(self):
        incorrect_dict = {'foo':[{'bar': 'baz'}, {'not':'a'}], 'real': 'response'}
        actual_response = convert_event_to_strings(incorrect_dict)
        expected_response = (None, None)
        self.assertEqual(actual_response, expected_response)
