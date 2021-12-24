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
    location = input("Where do you want to eat? \n")
    return location


def get_location():
    location = which_location()
    BASE_URL = "http://api.openweathermap.org/geo/1.0/direct?"
    URL = BASE_URL + "q=" + location + "&appid=" + os.environ['OPEN_WEATHER']
    response = requests.get(URL)
    latitude = response.json()[0]["lat"]
    longitude = response.json()[0]["lon"]
    if response.status_code != 200:
        print("Error in the HTTP request")
    return latitude, longitude


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


def get_restaurants(cuisine_type, location):
    """Returns restaurants from Travel Advisor from user's inputed cuisine choice"""
    latitude = float(location[0])
    longitude = float(location[1])
    print(latitude)
    querystring = {
        "latitude": f"{latitude}",
        "longitude": f"{longitude}",
        "limit": "50",
        "currency": "CAD",
        "distance": "5",
        "restaurant_tagcategory": f"{CUISINE_CODES[cuisine_type]}",
        "open_now": "false",
        "lunit": "km",
        "lang": "en_US",
        "min_rating": "4"
    }

    headers = {
        'x-rapidapi-host': "travel-advisor.p.rapidapi.com",
        'x-rapidapi-key': "0cc3dcdeaamsh25496be4808dcb0p1f4428jsnc2ff3691a620"
    }

    restaurants = requests.request("GET", "https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng", headers=headers, params=querystring)

    restaurants = restaurants.json()['data']
    return restaurants


def choose_restaurant():
    location = get_location()
    cuisine_type = which_cuisine()
    restaurants = get_restaurants(cuisine_type, location)
    chosen_restaurant = random.choice(restaurants)
    return chosen_restaurant


if __name__ == "__main__":
    restaurant = choose_restaurant()
    print(restaurant["name"])
    print(restaurant["website"])
