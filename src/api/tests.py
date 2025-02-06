from django.test import TestCase
import requests



API_KEY = '5b3ce3597851110001cf6248e939ea4a3aa04384b8cc376b5158eeb1'
url = 'https://api.openrouteservice.org/v2/directions/driving-car'
headers = {
    'Authorization': API_KEY,
}
params = {
    'start': '-122.42,37.77',  # San Francisco
    'end': '-104.99,39.74',    # Denver
}

response = requests.get(url, headers=headers, params=params)
print(response.json())