from rest_framework.response import Response
from rest_framework.views import APIView
from api.services import get_route
from api.utils import get_fuel_stops

class RouteAPI(APIView):
    def get(self, request):
        start = request.GET.get("start")
        end = request.GET.get("end")

        if not start or not end:
            return Response({"error": "Missing start or end location"}, status=400)

        route = get_route(start, end)
        fuel_stops, total_cost = get_fuel_stops(route[0]["legs"][0]["steps"])

        return Response({
            "route": route[0]["overview_polyline"]["points"],
            "fuel_stops": [{"name": stop.name, "price": stop.retail_price} for stop in fuel_stops],
            "total_cost": total_cost
        })
