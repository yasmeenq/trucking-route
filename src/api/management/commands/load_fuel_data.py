import csv
import os
from django.core.management.base import BaseCommand
from api.models import TruckStop
from api.services import get_coordinates  # Import your geocoding function

class Command(BaseCommand):
    help = "Load fuel price data from CSV into the TruckStop model"

    def handle(self, *args, **kwargs):
        file_path = os.path.join("data", "fuel_prices.csv")

        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                full_address = f"{row['Address']}, {row['City']}, {row['State']}"
                print(f"\nProcessing: {full_address}")  # Debug

                # Fetch coordinates
                coordinates = get_coordinates(full_address)
                
                if coordinates:
                    latitude = coordinates.get("lat")
                    longitude = coordinates.get("lng")
                else:
                    latitude, longitude = None, None
                
                print(f"Retrieved coordinates: {latitude}, {longitude}")  # Debug

                # Store in database
                obj, created = TruckStop.objects.update_or_create(
                    opis_id=row["OPIS Truckstop ID"],
                    defaults={
                        "name": row["Truckstop Name"],
                        "address": row["Address"],
                        "city": row["City"],
                        "state": row["State"],
                        "rack_id": row["Rack ID"] or None,
                        "retail_price": row["Retail Price"] or None,
                        "latitude": latitude,
                        "longitude": longitude,
                    },
                )

                if created:
                    print(f"✅ Created: {obj.name} | lat: {obj.latitude}, lng: {obj.longitude}")
                else:
                    print(f"🔄 Updated: {obj.name} | lat: {obj.latitude}, lng: {obj.longitude}")

        self.stdout.write(self.style.SUCCESS("Successfully loaded fuel data with coordinates"))

