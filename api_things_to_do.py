"""
We'll be using the ticketmaster API to search for things to do in the querant location. 

searches can be done using city name

Examples: 

Search for music events in the Los Angeles area
 https://app.ticketmaster.com/discovery/v2/events.json?
classificationName=music&dmaId=324&apikey=${TICKETMASTER_KEY}
Get a list of all events for Adele in Canada
 https://app.ticketmaster.com/discovery/v2/events.json?
attractionId=K8vZ917Gku7&countryCode=CA&apikey=${TICKETMASTER_KEY}


conn.execute("INSERT INTO things_to_do VALUES (?,?,?)", (save_id, event_title, event_url))

All key-value pairs are delineated by '&'.  Start with the '*.json' and '?'
"""
"""
:input: city_name from api_geolocation
:output: str name o
"""



import os
from api_handler import API_request
from ui import message
from random import randint

root_url = 'https://app.ticketmaster.com/discovery/v2/'
key = os.environ.get("TICKETMASTER_KEY")


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
    # TODO Handle errors from different structure
    return chosen_event

def convert_event_to_strings(event):
    '''
    :input: [dict] event info
    :outputs: [str] event name, [str] event_url   
    '''
    event_name = event['name']
    event_url = event['url']
    return event_name, event_url

def get_random_local_event(city_name):
    '''
    High-level method that calls on the other methods in this module.
      Intended to connect to main.py.
    :input: [str] 
    :outputs: [str]
    '''
    response = get_events_request_from_city_name(city_name)
    try:
        event = get_random_event_from_response(response)
    except Exception as e:
        message(e) # TODO - User friendly error handling
    
    event_name, event_url = convert_event_to_strings(event)
    return event_name, event_url
   

    # return event_str to api_handler -> main.py#