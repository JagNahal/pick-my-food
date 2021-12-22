import os
import requests
import random

CUISINE_CODES = {
    'ASIAN': 10659,
    'INDIAN': 10346,
    'SEAFOOD': 10643,
    'THAI': 10660,
    'JAPANESE': 5473,
    'EUROPEAN': 10654,
    'AMERICAN': 9908,
    'CHINESE': 5379,
    'SUSHI': 10653,
    'ITALIAN': 4617,
    'FRENCH': 5086,
    'FAST FOOD': 10646,
    'KOREAN': 10661,
    'VIETNAMESE': 10675,
}

def which_location():
  pass

def get_location():
  pass

def get_cuisines_prompt():
    """Returns a friendly sorted list of cuisine options for display in prompt"""
    cuisines = []
    for cuisine in CUISINE_CODES:
        cuisines.append(cuisine)
    cuisines_prompt = '\n'.join(sorted(cuisines)).title()
    return cuisines_prompt


def which_cuisine():
    """Grabs user input and returns the cuisine type chosen."""
    cuisine_type = input(
        f"Which Cuisine?\n\n{get_cuisines_prompt()}\n\n> ").upper()
    return cuisine_type


def get_restaurants(cuisine_type):
    """Returns restaurants from Travel Advisor from user's inputed cuisine choice"""

    query_string = {
        "bl_latitude": "49.204589",
        "tr_latitude": "49.301397",
        "bl_longitude": "-123.223932",
        "tr_longitude": "-122.702477",
        "min_rating": "4",
        "restaurant_tagcategory_standalone": "10591",
        "restaurant_tagcategory": "10591",
        "limit": "50",
        "currency": "CAD",
        "combined_food": f"{CUISINE_CODES[cuisine_type]}",
        "lunit": "km",
        "lang": "en_US"
    }

    headers = {
        'x-rapidapi-host': "travel-advisor.p.rapidapi.com",
        'x-rapidapi-key': os.environ['TRAVEL_ADVISOR']
    }

    restaurants = requests.request(
        "GET",
        "https://travel-advisor.p.rapidapi.com/restaurants/list-in-boundary",
        headers=headers,
        params=query_string)

    restaurants = restaurants.json()['data']

    return restaurants


def choose_restaurant():
    cuisine_type = which_cuisine()
    restaurants = get_restaurants(cuisine_type)
    chosen_restaurant = random.choice(restaurants)
    return chosen_restaurant


if __name__ == "__main__":
    restaurant = choose_restaurant()
    print(restaurant["name"])
    print(restaurant["website"])
