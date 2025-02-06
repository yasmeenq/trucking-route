from math import radians, cos
from api.models import TruckStop
from decimal import Decimal 

MAX_RANGE_MILES = 500  # Car can travel 500 miles per fuel stop
MPG = 10  # 10 miles per gallon
TANK_CAPACITY = MAX_RANGE_MILES / MPG  # Max gallons per fill-up

def get_fuel_stops(route):
    fuel_stops = []
    total_cost = 0
    distance_traveled = 0

    for step in route:
        distance_traveled += step["distance"]["value"] / 1609.34  # Convert meters to miles

        if distance_traveled >= MAX_RANGE_MILES:
            nearest_stop = TruckStop.objects.order_by("retail_price").first()
            fuel_stops.append(nearest_stop)
            total_cost += nearest_stop.retail_price * Decimal(TANK_CAPACITY)
            distance_traveled = 0  # Reset after fueling

    return fuel_stops, total_cost
