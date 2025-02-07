import googlemaps
from django.conf import settings


GMAPS_CLIENT = googlemaps.Client(key = settings.GOOGLE_MAPS_API_KEY)

def get_route(start: str, end: str):
    """Fetch route details from Google Maps API"""
    directions = GMAPS_CLIENT.directions(start, end, mode="driving")
    return directions

def get_coordinates(address: str):
    """Convert address to latitude & longitude"""
    geocode_result = GMAPS_CLIENT.geocode(address)
    if geocode_result:
        return geocode_result[0]["geometry"]["location"]
    return None


#Documentations:
#https://developers.google.com/maps/documentation/geocoding/start
#https://developers.google.com/maps/documentation/directions/start

#example of get_coordinates response:
#{'lat': 36.5515885, 'lng': -95.224598}

#example of get_route response:
# {
#   "routes": [
#     {
#       "bounds": {
#         "northeast": {
#           "lat": 37.7749,
#           "lng": -122.4194
#         },
#         "southwest": {
#           "lat": 34.0522,
#           "lng": -118.2437
#         }
#       },
#       "legs": [
#         {
#           "distance": {
#             "text": "381 mi",
#             "value": 613838
#           },
#           "duration": {
#             "text": "5 hours 57 mins",
#             "value": 21420
#           },
#           "end_address": "Los Angeles, CA",
#           "end_location": {
#             "lat": 34.0522,
#             "lng": -118.2437
#           },
#           "start_address": "San Francisco, CA",
#           "start_location": {
#             "lat": 37.7749,
#             "lng": -122.4194
#           },
#           "steps": [
#             {
#               "distance": {
#                 "text": "1.0 mi",
#                 "value": 1609
#               },
#               "duration": {
#                 "text": "4 mins",
#                 "value": 240
#               },
#               "end_location": {
#                 "lat": 37.7763,
#                 "lng": -122.4192
#               },
#               "html_instructions": "Head east on Market St toward 5th St"
#             },
#             {
#               "distance": {
#                 "text": "5.2 mi",
#                 "value": 8368
#               },
#               "duration": {
#                 "text": "12 mins",
#                 "value": 720
#               },
#               "end_location": {
#                 "lat": 37.7628,
#                 "lng": -122.4591
#               },
#               "html_instructions": "Turn right onto 6th St"
#             }
#             // More steps...
#           ]
#         }
#       ]
#     }
#   ]
# }
