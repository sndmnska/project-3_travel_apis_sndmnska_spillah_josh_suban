"""
We'll be using the ticketmaster API to search for things to do in the querant location. 

searches can be done using latlong, radius. 

Examples: 

Search for music events in the Los Angeles area
 https://app.ticketmaster.com/discovery/v2/events.json?
classificationName=music&dmaId=324&apikey=${API_KEY}
Get a list of all events for Adele in Canada
 https://app.ticketmaster.com/discovery/v2/events.json?
attractionId=K8vZ917Gku7&countryCode=CA&apikey=${API_KEY}

All key-value pairs are delineated by '&'.  Start with the '*.json' and '?'

:input: city_name from api_geolocation
:output: str name of the top (1) event returned 
"""



import os
from api_handler import API_request
from ui import message
from random import randint

root_url = 'https://app.ticketmaster.com/discovery/v2/'
key = os.environ.get("TICKETMASTER_KEY")

def import_city_name():
    '''
    Get city name from geolocation search
    :output: [str] city name
    '''

    # TODO FIXME - Delete these next few lines when ready to test with api_geolocation.py
    # For testing purposes, assign a known working city name. 
    sample_city = 'Minneapolis'  # Minneapolis, MN, USA [44.9772995, -93.2654692]
    city_name = sample_city

    return city_name

def get_events_request_from_city_name(city_name):
    '''
    Request json response from the Ticketmaster API: All events within 30 miles of requested location.  
        Convert response to dictionary, or send errors as applicable.
    :input: city_name
    :output: [dict] response
    '''
    url = root_url + 'events' # build the root url in this function, in case the app in the future wants to use more than one request type.
    query = {'radius': 30, 'unit':'miles','city': city_name, 'apikey': key}

    response = API_request(url, query)
    if response is None:
        return # TODO Handle a Non-response
    else: 
        return response

    

def get_random_event_from_response(response):    
    '''
    Extract a random event from a successful response.
        Send error if unexpected structure
    :input: response dictionary
    :outputs: [dict] event key:value pair, [dict] error information
    '''
    print(response)
    events = response['_embedded']['events']
    event_count = len(events)
    rand_event_choice = randint(1, event_count)
    chosen_event = events[rand_event_choice]
    
    return chosen_event

def convert_event_name_to_str(event):
    '''
    :input: [dict] event key:value pair
    :output: [str] event name, capitalized   
    '''
    event


    return event_name

def main():
    city_name = import_city_name() 

    response = get_events_request_from_city_name(city_name)
    try:
        event = get_random_event_from_response(response)
    except Exception as e:
        message(e)

main()        

    # event_str = convert_event_to_str(event)
    # return event_str to api_handler -> main.py