import requests
"""
API Handler

This module handles the subprocesses of the API caller modules.   

As one request for a destination calls three separate APIs, this module can collect the total data of those calls, 
    including any errors or incomplete data.   

If one or more APIs fails, what does this return?  I would argue that, if possible, it would be nice to get whatever data we can 
    even if one or more of these APIs are down. 

API geolocation call -> 

"""

def handle_request(url, params):
    '''
    Manages error handling for our requests.
    :param url: API URL
    :param params: API parameters
    :return: json if successful or None if not.
    '''
    response = requests.get(url, params)

    if response.status_code == 200:
        return response.json()
    if response.status_code == 404:
        return None