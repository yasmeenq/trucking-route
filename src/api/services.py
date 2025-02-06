import googlemaps
from django.conf import settings

GMAPS_CLIENT = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

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
