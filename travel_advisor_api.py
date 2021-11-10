"""import requests

url = "https://travel-advisor.p.rapidapi.com/restaurants/list-in-boundary"

querystring = {"bl_latitude":"49.177215","tr_latitude":"49.296695","bl_longitude":"-123.18682","tr_longitude":"-122.882894","min_rating":"4","restaurant_tagcategory_standalone":"10591","restaurant_tagcategory":"10591","limit":"50","currency":"CAD","combined_food":"american","lunit":"km","lang":"en_US"}

headers = {
    'x-rapidapi-host': "travel-advisor.p.rapidapi.com",
    'x-rapidapi-key': "0cc3dcdeaamsh25496be4808dcb0p1f4428jsnc2ff3691a620"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
print(querystring)"""