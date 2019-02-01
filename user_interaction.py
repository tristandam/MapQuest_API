# This module is where the user inputs the locations of interest, and recieves the output handled by the output module.

import mapquest_api


def user_interface() -> None:
    'Initializes the main program and takes in user input'
    num_of_locations = int(input())
    locations = mapquest_api.get_locations(num_of_locations)
    num_of_outputs = int(input())
    outputs = mapquest_api.get_outputs(num_of_outputs)

    print(mapquest_api.build_url(locations))
    mapquest_data = mapquest_api.parse_url(mapquest_api.build_url(locations))




if __name__ == '__main__':
    user_interface()

