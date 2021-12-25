import requests

url = "https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng"

querystring = {
    "latitude": "12.91285",
    "longitude": "100.87808",
    "limit": "50",
    "currency": "CAD",
    "distance": "5",
    "restaurant_tagcategory": "10591",
    "open_now": "false",
    "lunit": "km",
    "lang": "en_US",
    "min_rating": "4"
}

headers = {
    'x-rapidapi-host': "travel-advisor.p.rapidapi.com",
    'x-rapidapi-key': "0cc3dcdeaamsh25496be4808dcb0p1f4428jsnc2ff3691a620"
}

restaurants = requests.request("GET", url, headers=headers, params=querystring)

print(restaurants.text)
