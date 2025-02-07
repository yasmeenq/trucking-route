from math import radians, cos, sin, sqrt, atan2
from api.models import TruckStop
from decimal import Decimal

MAX_RANGE_MILES = 500  # Car can travel 500 miles per fuel stop
MPG = 10  # 10 miles per gallon
TANK_CAPACITY = MAX_RANGE_MILES / MPG  # Max gallons per fill-up (50)

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate the distance between two coordinates in miles"""
    R = 3958.8  # Radius of the Earth in miles

    lat1, lon1 = float(lat1), float(lon1)
    lat2, lon2 = float(lat2), float(lon2)

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) * sin(dlat / 2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) * sin(dlon / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


def get_optimal_fuel_stops(route):
    fuel_stops = []
    total_cost = 0
    distance_traveled = 0

    for step in route:
        distance_traveled += step["distance"]["value"] / 1609.34  # Convert meters to miles

        if distance_traveled >= MAX_RANGE_MILES:
            current_location = step["end_location"]
            print(f"Current Location: {current_location}")

            # Check if the coordinates of current location are valid
            if current_location.get("lat") is None or current_location.get("lng") is None:
                continue 

            # Get all truck stops that are within range of the current location
            nearest_stops = TruckStop.objects.all()

            # Filter stops by proximity, ensuring the stop coordinates are valid
            nearby_stops = [
                stop for stop in nearest_stops if stop.latitude is not None and stop.longitude is not None and calculate_distance(
                    current_location["lat"], current_location["lng"],
                    stop.latitude, stop.longitude
                ) <= MAX_RANGE_MILES
            ]
            
            # print(f"Nearby Stops: {nearby_stops}")

            # Sort by price first, then by distance
            sorted_stops = sorted(nearby_stops, key=lambda stop: (
                stop.retail_price,  # Prefer cheaper price
                calculate_distance(current_location["lat"], current_location["lng"], stop.latitude, stop.longitude)  # Prefer closer distance
            ))

            # print(f"Sorted Stops: {sorted_stops}")

            # Ensure that there is at least one valid stop
            if sorted_stops:
                # Pick the cheapest fuel stop within range
                nearest_stop = sorted_stops[0]  # Pick the closest and cheapest fuel stop
                fuel_stops.append(nearest_stop)
                total_cost += nearest_stop.retail_price * Decimal(TANK_CAPACITY)
                distance_traveled = 0  # Reset after fueling
            else:
                print(f"No valid fuel stops found for current location: {current_location}")

    return fuel_stops, total_cost
