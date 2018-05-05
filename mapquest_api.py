#mapquest_api.py


#A module that interacts with the Open MapQuest APIs.
# This is where you should do things like building URLs, making HTTP requests, and parsing JSON responses.


import json
import urllib.parse
import urllib.request


MAPQUEST_API_KEY = 'LavK4KKvuP4NEHf7h8VWTq8oGLakIFmA'


def get_locations(number_of_locations:int)->list:
    'Given a number of locations, return a list containing those locations'
    locations = []
    if number_of_locations < 2:
        print("Please enter 2 or more locations.")
    else:
        for user_input in range(number_of_locations):
            location = input()
            locations.append(location)
        return locations

def get_outputs(number_of_outputs:int)->list:
    'Given a number of outputs, return a list containing which outputs to use'
    outputs = []
    if number_of_outputs < 1:
        print("Please request a number of outputs greater than or equal to one.")
    else:
        for user_input in range(number_of_outputs):
            output = input()
            outputs.append(output)
        return outputs


def build_url()->str:
    'Takes your base URL, adds the necessary parameters to make an API Request to MapQuest'
    query_parameters = [('key',MAPQUEST_API_KEY), ]


