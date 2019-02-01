


# This is the module of my program that interacts with the MapQuest API.
# Here, I build my URL using my API key, use that URL to make an HTTP request from which I store the data in JSON format.


import json
import urllib.parse
import urllib.request


MAPQUEST_API_KEY = 'LavK4KKvuP4NEHf7h8VWTq8oGLakIFmA'
base_mapquest_url = "http://open.mapquestapi.com/directions/v2"
base_elevation_url = "http://open.mapquestapi.com/elevation/v1"



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

def build_elevation_url(lat_long_pairs:list)->str:
    'Takes the base url, adds the necessary latitude longitude pairs to construct an elevation url'

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

def lat_long_list(json_dict:dict)->list:
    'Given a dictionary, returns a string of latitude longitude pairs needed for elevation output'
    lat_long_str = ''
    for location in json_dict["route"]["locations"]:
        lat = location['displayLatLng']['lat']
        lng = location['displayLatLng']['lng']
        lat_long_str += str(lat) + ","
        lat_long_str += str(lng) + ","
    return lat_long_str

