from __future__ import print_function
import requests
import json
import sys
import os
addr = 'http://127.0.0.1:5000'
"""
signup_url = addr + '/signUp'
response = requests.post(signup_url, params={"email": "john@gmail.com", "password": "password", "genre": "Action", "maxDistance": 2, "maxPrice": 30})
print("Response is", response)
print(json.loads(response.text))
"""
login_url = addr + '/login'
response = requests.post(login_url, params={'username': 'john@gmail.com', 'password': 'password'})
print("Response is", response)
print(json.loads(response.text))

dashboard_url = addr + '/dashboard'
response = requests.get(dashboard_url)
print("Response is", response)
print(json.loads(response.text))

preferences_url = addr + '/updatePreferences'
response = requests.post(preferences_url, params={'genre': 'Action', 'maxDistance': 3, 'maxPrice': 30})
print("Response is", response)
print(json.loads(response.text))

signOut_url = addr + '/signOut'
response = requests.post(signOut_url)
print("Response is", response)