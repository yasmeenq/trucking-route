from django.urls import path
from api.views import get_route_and_fuel_stops

urlpatterns = [
    path('route/', get_route_and_fuel_stops, name='route'),
]