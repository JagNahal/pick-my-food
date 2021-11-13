from __future__ import print_function
import price_cuisine_functions
import food_options
import requests
import random
import cuisine_codes

initialize = input()
if initialize == ".":
    cost = price_cuisine_functions.price()
    cuisine_type = price_cuisine_functions.cuisine()
    # dish_type = price_cuisine_functions.dish()






# if cuisine_type == 'KOREAN':
#     if cost == 'C':
#         print('Daniel\'s House')
#     elif cost == 'N':
#         print('Nadri')
#     elif cost == 'F':
#         print('Kook KBBQ')

# if cuisine_type == 'AMERICAN':
#     if cost == 'C':
#         print(food_options.cheap_american.pop())
#     elif cost == 'N':
#         print('Cactus Club')
#     elif cost == 'F':
#         print('Hy\'s Steakhouse')

# if cuisine_type == 'JAPANESE':
#     if dish_type == 'ramen':
#         if cost == 'C':
#             print('idk')
#         elif cost == 'N':
#             print(food_options.ramen.pop().capitalize())
#         elif cost == 'F':
#             print('somewhere fancy')
#     elif dish_type == 'sushi':
#         if cost == 'C':
#             print('idk')
#         elif cost == 'N':
#             print('sushi cali')
#         elif cost == 'F':
#             print('somewhere fancy')
#     elif dish_type != 'ramen' or 'sushi':
#         if cost == 'C':
#           print('idk')
#         elif cost == 'N':
#           print(food_options.normal_asian.pop().capitalize())
#         elif cost == 'F':
#             print('somewhere fancy')

url = "https://travel-advisor.p.rapidapi.com/restaurants/list-in-boundary"

querystring = {"bl_latitude":"49.177215","tr_latitude":"49.296695","bl_longitude":"-123.18682","tr_longitude":"-122.882894","min_rating":"4","restaurant_tagcategory_standalone":"10591","restaurant_tagcategory":"10591","limit":"50","currency":"CAD","combined_food":"10646","lunit":"km","lang":"en_US"}

headers = {
    'x-rapidapi-host': "travel-advisor.p.rapidapi.com",
    'x-rapidapi-key': "0cc3dcdeaamsh25496be4808dcb0p1f4428jsnc2ff3691a620"
    }

restaurant_codes = {'VIETNAMESE':10675, 'ASIAN':10659, 'INDIAN':10346}

querystring['combined_food'] = restaurant_codes[cuisine_type]

response = requests.request("GET", url, headers=headers, params=querystring)

restaurants = response.json()['data']

print(random.choice(restaurants)["name"])


    

