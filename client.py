from __future__ import print_function
import requests
import json
import sys
import os
addr = 'http://127.0.0.1:5000'
"""
#user registers
signup_url = addr + '/signUp'
response = requests.post(signup_url, params={"email": "john@gmail.com", "password": "password", "genre": "Action", "maxDistance": 2, "maxPrice": 30})
print("Response is", response)
print(json.loads(response.text))
"""
#user raises a login request and begins the session
login_url = addr + '/login'
response = requests.post(login_url, params={'username': 'john@gmail.com', 'password': 'password'})
print("Login Response is", response)
print(json.loads(response.text))

#user chooses from the list of shows displayed using index linked to the select button
show_url = addr + '/show'
response = requests.get(show_url, params={'index': 0})
print("Show Response is", response)
print(json.loads(response.text))

#user chooses number of slots and the food quantity for the selected show
show_url = addr + '/show'
food_quantity_list =[1,1]
response = requests.post(show_url, params={'num_slots': 1,'food_quantity_list:0': 1, 'food_quantity_list:1': 1})
print("Show Total Cost Response is", response)
print(json.loads(response.text))

#user raises request to update their preferences
purchase_url = addr + '/purchase'
response = requests.post(purchase_url, params={'cardNumber': '100000000000000', 'securityCode': '3333', 'expireDate': '02/20' , 'cardType':'debit'})
print("Update purchase Response is", response)
print(json.loads(response.text))

#user raises request to view their profile dashboard which contains current preferences and purchase history
dashboard_url = addr + '/dashboard'
response = requests.get(dashboard_url)
print("Daskboard Response is", response)
print(json.loads(response.text))

#user raises request to cancel their purchase
preferences_url = addr + '/cancelPurchase'
response = requests.post(preferences_url, params={'index': 0})
print("Deleted Purchase Response is", response)
print(json.loads(response.text))


#user ends his session
signOut_url = addr + '/signOut'
response = requests.post(signOut_url)
print("Sign out Response is", response)

