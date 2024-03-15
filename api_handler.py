import requests
from ui import message
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

    # TODO This code is brittle.  Can we include status code ranges, and an else function for handling other codes?
    # Common successful codes include 200, 201, 204, etc.  There are many failure status codes as well. 
    # 200 - successful, with data
    # 204 - successful, no data to show
    
    if response.status_code == 200:
        return response.json()
    if response.status_code == 404:
        return None

def API_request(url, params):
    '''
        Manages error handling for the data of our requests.
        :param url: API URL
        :param params: API parameters
        :return: data if successful or None if not.
        '''

    data = None

    try:
        data = handle_request(url, params)
    except requests.exceptions.ConnectionError as e:
        message('Please check your internet connection!')
        return None
    except Exception:
        message('An Unknown error has occurred!')
        return None

    if not data or len(data) == 0:
        return None
    else:
        return data