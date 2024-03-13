"""
We'll be using the ticketmaster API to search for things to do in the querant location. 

searches can be done using latlong, radius. 

Examples: 

Search for music events in the Los Angeles area
 https://app.ticketmaster.com/discovery/v2/events.json?
classificationName=music&dmaId=324&apikey=0tWsbiMH7lHmQdr7K1P7vfUMNWew
iJWQ
Get a list of all events for Adele in Canada
 https://app.ticketmaster.com/discovery/v2/events.json?
attractionId=K8vZ917Gku7&countryCode=CA&apikey=0tWsbiMH7lHmQdr7K1P7vfU
MNWewiJWQ

All key-value pairs are delineated by '&'.  Start with the '*.json' and '?'

:Input: latlong from api_geolocation
:output: str name of the top (1) event returned 
"""


latlong = []

root_url = 'https://app.ticketmaster.com/discovery/v2/'

# FIXME - Delete these lines when ready to test with api_geolocation.py
# For testing purposes, assign a known working lat_long tuple. 
sample_latlong = [44.9772995, -93.2654692]  # Minneapolis, MN, USA
latlong = sample_latlong


def get_request_from_latlong(latlong):
    pass

def get_top_event_from_response(response):
    pass

def convert_event_to_str(event):
    return string

def main():
    get_request_from_latlong(latlong)
    get_top_event_from_response(response)
    event_str = convert_event_to_str(event)
    # return event_str to api_handler -> main.py





if __name__ == "__main__":
    main()