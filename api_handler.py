import requests
import logging
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

    # Status code categories:  <https://restfulapi.net/http-status-codes/>
    # 1xx: Informational  |  2xx: Success  | 3xx: Redirection | 4xx: Client Error | 5xx: Server Error
    status_code = response.status_code

    if status_code == 200: # Status 200 - OK
        return response.json()
    elif status_code > 200 and status_code > 300:  # Successful response, but not '200 - OK'.
        message(f'Success, but something\'s changed... -- Response Status code: {status_code}')
        return response.json()
    elif status_code >= 300 and status_code < 600:
        if status_code < 400: # Redirection Category
            message(f'Response Status code: {status_code}. "Redirection" Please search online for more details.')
                # A list of common 400 codes
            if status_code >= 400 and status_code < 500:
                if status_code == 400: # 400 Bad Request (Incorrect Syntax)
                    message(f'Error 400 - Bad Request. Incorrect request syntax. Please fix.')
                if status_code == 401: # 401 Unauthorized
                    message(f'Error 401 Unauthorized request: Needs user authentication information. \n\t*****Do you have your API key configured correctly?')
                if status_code == 403: # 403 Forbidden - API key not accepted
                    message(f'Error 403 Forbidden request: API Key not authorized for a request. Please try reentering your API key, or get a new one.')
                if status_code == 404: # 404 Not Found
                    message(f'Error 404 Not Found: Requested api NOT found at requested url.')
            else:  # Other Client Error 4xx
                message(f'Client Error while retrieving the API request -- Error {status_code}. Please see online for more information.')
        if status_code >= 500 and status_code < 600:
            message(f'Error {status_code} - A Server Error Occurred. ')
        return None
    else:
        message(f'ERROR {status_code}: Server responded with status code {status_code}. Please see online for more infomation.')




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