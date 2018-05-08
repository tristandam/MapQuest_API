#mapquest_api.py


#A module that interacts with the Open MapQuest APIs.
# This is where you should do things like building URLs, making HTTP requests, and parsing JSON responses.


import json
import urllib.parse
import urllib.request


MAPQUEST_API_KEY = 'LavK4KKvuP4NEHf7h8VWTq8oGLakIFmA'
base_mapquest_url = "http://open.mapquestapi.com/directions/v2"



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


def locations_to_tuples(locations:list)-> list:
    'Given a list of locations, returns a list of tuples with the locations in query format'
    location_tuples = []
    for location in locations:
        if location == locations[0]:
            first_location = ("from",location)
            location_tuples.append(first_location)
        else:
            remaining_locations = ("to", location)
            location_tuples.append(remaining_locations)
    return location_tuples

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



def build_url(list_of_locations:list)->str:
    'Takes your base URL, adds the necessary parameters to make an API Request to MapQuest'
    key_parameter = [('key',MAPQUEST_API_KEY)]
    locations_to_use = locations_to_tuples(list_of_locations)
    query_parameters = key_parameter+locations_to_use

    return base_mapquest_url + '/route?' + urllib.parse.urlencode(query_parameters)

def parse_url(page_url:str)-> dict:
    'Takes a url and returns a python dictionary representing the parsed JSON response'
    response = None

    try:
        response = urllib.request.urlopen(page_url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()

