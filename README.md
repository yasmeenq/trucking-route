



1. open src folder 
2. create virtual environment: `py -m venv env` 
3. activate it: `env/Scripts/Activate`
4. install Django `pip install django`
5. requirements: `pip freeze > requirements.txt`  
6. `django-admin startproject games src`  
7. publish your website: `py src/manage.py runserver` 
8. open website from chrome: http://127.0.0.1:8000/

API documentation:
https://giscience.github.io/openrouteservice/api-reference/endpoints/directions/


dependencies:
pip install django djangorestframework requests pandas googlemaps

django → Main framework
djangorestframework → API development
requests → Making API calls
pandas → Reading CSV files
googlemaps → Google Maps API



📌 Step 1: Install Dependencies
pip install django djangorestframework requests pandas googlemaps
pip install geopy


📌 Step 2: Create Django Project and App

django-admin startproject fuel_optimizer_project
cd fuel_optimizer_project
django-admin startapp api

Add fuel_api to INSTALLED_APPS in settings.py


📌 Step 3: Define Models (models.py)

cd src 
python manage.py makemigrations
python manage.py migrate

📌 Step 4: Load CSV Data (management/commands/load_fuel_data.py)
Inside fuel_api/management/commands/, create load_fuel_data.py:
Run it:
python manage.py load_fuel_data


📌 Step 5: Google Maps API Call (services.py)
Create fuel_api/services.py:

📌 Step 6: Calculate Fuel Stops (utils.py)
Create fuel_api/utils.py:

📌 Step 7: Build API (views.py)

📌 Step 8: Configure URLs (urls.py)

📌 Step 9: Add API Key to settings.py
import os
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

📌 Step 10: Run the Server
python manage.py runserver


http://127.0.0.1:8000/route/?start=New+York,NY&end=Los+Angeles,CA



📌 Expected API Response
{
  "route": "encoded_polyline",
  "fuel_stops": [
    {"name": "WOODSHED OF BIG CABIN", "price": 3.00},
    {"name": "PILOT TRAVEL CENTER", "price": 3.89}
  ],
  "total_cost": 600.50
}