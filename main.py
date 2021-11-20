import os
import requests
import random
my_secret = os.environ['API Key']
def which_cuisine():
  """User inputs which cuisine they want to eat"""
  cuisine_type = input("Which Cuisine?\n\nAmerican\nAsian\nChinese\nFrench\nFast Food\nIndian\nItalian\nJapanese\nKorean\nSeafood\nSushi\nThai\nVietnamese\n\n").upper()
  return cuisine_type

def get_restaurants():  
  """Returns restaurnts from Travel Advisor from user's inputted cuisine choice"""
  
  querystring = {"bl_latitude":"49.204589","tr_latitude":"49.301397","bl_longitude":"-123.223932","tr_longitude":"-122.702477","min_rating":"4","restaurant_tagcategory_standalone":"10591","restaurant_tagcategory":"10591","limit":"50","currency":"CAD","combined_food":"10646","lunit":"km","lang":"en_US"}

  #Add japanese and mexican cuisine types
  restaurant_codes = {'VIETNAMESE':10675, 'ASIAN':10659,'INDIAN':10346, 'SEAFOOD':10643, 'THAI':10660, 'AMERICAN':9908, 'CHINESE':5379,'SUSHI':10653, 'ITALIAN':4617, 'FRENCH':5086, 'FAST FOOD':10646, 'KOREAN':10661,}

  headers = {
    'x-rapidapi-host': "travel-advisor.p.rapidapi.com",
    'x-rapidapi-key': my_secret
    }
  cuisine_type = which_cuisine()
  querystring['combined_food'] = restaurant_codes[cuisine_type]

  restaurants = requests.request("GET", "https://travel-advisor.p.rapidapi.com/restaurants/list-in-boundary", headers=headers, params=querystring)

  print(restaurants)

  restaurants = restaurants.json()['data']

  print(restaurants)
  return restaurants


def choose_restaurant():
  restaurants = get_restaurants()
  print(random.choice(restaurants)["name"])

choose_restaurant()

