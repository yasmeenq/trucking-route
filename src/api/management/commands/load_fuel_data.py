import csv
import os
from django.core.management.base import BaseCommand
from api.models import TruckStop

class Command(BaseCommand):
    help = "Load fuel price data from CSV"

    def handle(self, *args, **kwargs):
        file_path = os.path.join('data', 'fuel_prices.csv')
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                TruckStop.objects.update_or_create(
                    opis_id=row["OPIS Truckstop ID"],
                    defaults={
                        "name": row["Truckstop Name"],
                        "address": row["Address"],
                        "city": row["City"],
                        "state": row["State"],
                        "rack_id": row["Rack ID"],
                        "retail_price": row["Retail Price"],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded fuel data'))
