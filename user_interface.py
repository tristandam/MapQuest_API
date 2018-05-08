#user_interface.py

# A module that reads the input and constructs the objects that will generate the program's output. '
#'This is the only module that should have an if __name__ == '__main__' block to make it executable;
# you would execute this module to run your program.

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

