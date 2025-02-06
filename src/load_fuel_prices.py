import csv
import os
import django
from api.models import FuelPrice

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fuel_optimizer.settings')
django.setup()

def load_fuel_prices(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            FuelPrice.objects.create(
                opis_truckstop_id = int(row['OPIS Truckstop ID']),
                truckstop_name = row['Truckstop Name'],
                address = row['Address'],
                city = row['City'],
                state = row['State'],
                rack_id = int(row['Rack ID']),
                retail_price = float(row['Retail Price'])
            )

if __name__ == '__main__':
    load_fuel_prices('path_to_your_csv_file.csv')