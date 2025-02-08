
### Loom video: 
https://www.loom.com/share/0153f6ebb2a94307b543a0ea4c59b974?sid=ca248b19-bb04-4fc5-b22f-02f3e8374dac

# Trucking Route Fuel Optimizer
This project provides a fuel optimization solution for long-haul trucking routes, using Google Maps API for geocoding and directions, along with fuel stop data and cost estimation.


## Steps to Set Up
1. git clone https://github.com/yasmeenq/trucking-route.git
2. create virtual environment: `py -m venv env` 
3. activate it: `env/Scripts/Activate`
4. pip install -r requirements.txt
5. open website on: http://127.0.0.1:8000/

## API documentation:
#https://developers.google.com/maps/documentation/geocoding/start
#https://developers.google.com/maps/documentation/directions/start

## Dependencies:
check requirements.txt


## Building Steps:
📌 Step 1: Install Dependencies
pip install django djangorestframework requests pandas googlemaps
pip install geopy


📌 Step 2: Create Django Project and App
django-admin startproject fuel_optimizer_project
cd fuel_optimizer_project
django-admin startapp api
Add api to INSTALLED_APPS in settings.py


📌 Step 3: Define Models (models.py)
after any change in models u need to makemigrations
cd src 
python manage.py makemigrations
python manage.py migrate


📌 Step 4: Populate CSV Data into models (management/commands/load_fuel_data.py)
Inside fuel_api/management/commands/, create load_fuel_data.py:
Run it:
python manage.py load_fuel_data


📌 Step 5: Google Maps API Call (services.py)
Create fuel_api/services.py:


📌 Step 6: Calculate Fuel Stops (utils.py)
Create fuel_api/utils.py:


📌 Step 7: Build API (views.py)


📌 Step 9: Add API Key to settings.py
import os
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")


📌 Step 10: Run the Server
python manage.py runserver


## Example API Request
http://127.0.0.1:8000/route/?start=New+York,NY&end=Los+Angeles,CA



## Expected API Response
{
  "route": "encoded_polyline",
  "fuel_stops": [
    {"name": "WOODSHED OF BIG CABIN", "price": 3.00},
    {"name": "PILOT TRAVEL CENTER", "price": 3.89}
  ],
  "total_cost": 600.50
}