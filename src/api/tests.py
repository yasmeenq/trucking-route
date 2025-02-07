

from api.models import TruckStop


stops = TruckStop.objects.all()
print(stops)


from api.services import get_coordinates

add = get_coordinates("I-44, EXIT 283 & US-69,Big Cabinm OK")
print(add)
#{'lat': 36.5515885, 'lng': -95.224598}