# MapQuest_API

These 3 modules comprise a project I wrote which was intended to experiment with API's in Python. It is a simple program
in which users enter in a start location, end location, and are returned an output containing step by step directions to the location
along with trip time, distance, and other trip details.

The bulk of this work is done in the "api_interaction.py" module. This is where I handle the various tasks needed to request
relevant information from the MapQuest API given the specific parameters the user asks for. I then parse the data in JSON format.

Then, the "trip_output.py" module works on converting the JSON data into readable strings for the user.

The "user_interaction.py" module is where the user is prompted to enter the locations of interest and recieve the data they are asking for.
