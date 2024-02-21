"""
API Handler

This module handles the subprocesses of the API caller modules.   

As one request for a destination calls three separate APIs, this module can collect the total data of those calls, 
    including any errors or incomplete data.   

If one or more APIs fails, what does this return?  I would argue that, if possible, it would be nice to get whatever data we can 
    even if one or more of these APIs are down. 

API geolocation call -> 

"""