import requests
from django.http import JsonResponse
from django.conf import settings
from api.models import FuelPrice

def get_route_and_fuel_stops(request):
    # Get start and end coordinates from query parameters
    start = request.GET.get('start')  # Format: "longitude,latitude"
    end = request.GET.get('end')      # Format: "longitude,latitude"

    # Call OpenRouteService API to get the route
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    headers = {
        'Authorization': settings.OPENROUTESERVICE_API_KEY,
    }
    params = {
        'start': start,
        'end': end,
    }
    response = requests.get(url, headers=headers, params=params)
    route_data = response.json()

    # Extract coordinates and distance
    coordinates = route_data['features'][0]['geometry']['coordinates']
    distance = route_data['features'][0]['properties']['segments'][0]['distance'] / 1609.34  # Convert meters to miles

    # Calculate fuel stops
    max_range = 500  # Vehicle range in miles
    fuel_stops = []
    current_distance = 0

    while current_distance < distance:
        remaining_distance = distance - current_distance
        if remaining_distance > max_range:
            # Find optimal fuel stop within the next 500 miles
            fuel_stop = find_optimal_fuel_stop(coordinates, current_distance, max_range)
            fuel_stops.append(fuel_stop)
            current_distance += max_range
        else:
            break

    # Calculate total fuel cost
    total_fuel_cost = (distance / 10) * min(fuel['retail_price'] for fuel in fuel_stops)

    # Return results
    return JsonResponse({
        'route': coordinates,
        'fuel_stops': fuel_stops,
        'total_fuel_cost': total_fuel_cost
    })

def find_optimal_fuel_stop(coordinates, current_distance, max_range):
    # Find the cheapest fuel stop within the next 500 miles
    fuel_prices = FuelPrice.objects.all()
    optimal_stop = min(fuel_prices, key=lambda x: x.retail_price)
    return {
        'name': optimal_stop.truckstop_name,
        'address': optimal_stop.address,
        'city': optimal_stop.city,
        'state': optimal_stop.state,
        'price': optimal_stop.retail_price
    }