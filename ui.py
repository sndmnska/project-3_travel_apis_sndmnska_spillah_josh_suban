"""
UI - User Interface

This module is used to accept inputs and display outputs to the user.
"""

def message(msg):
    ''' 
    Prints a message for the user
     :param msg: the message to print
    '''
    print(msg)

def user_question(q):
    '''
    Asks user a question and prompts a response
     :param q: The question to ask the useer
     :return: The user's input response
    '''
    user_response = input(q)
    return user_response
