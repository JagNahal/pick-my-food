import random
"""⢰⣶⠶⢶⣶⣶⡶⢶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡶⠶⢶⣶⣶⣶⣶
⠘⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⠿⠄⠄⠄⠈⠉⠄⠄⣹⣶⣿⣿⣿⣿⢿
⠄⠤⣾⣿⣿⣿⣿⣷⣤⡈⠙⠛⣿⣿⣿⣧⣀⠠⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶
⢠⠄⠄⣀⣀⣀⣭⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣤⣿⣿⠉⠉⠉⢉⣉⡉⠉⠉⠙⠛⠛
⢸⣿⡀⠄⠈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣷⣾⣿
⢸⣿⣿⣿⣿⣿⣿⣿⣿⠛⢩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢸⣿⣿⣿⣿⣿⡿⣿⣿⣴⣿⣿⣿⣿⣄⣠⣴⣿⣷⣭⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠸⠿⣿⣿⣿⠋⣴⡟⠋⠈⠻⠿⠿⠛⠛⠛⠛⠛⠃⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢸⣿⣿⣿⡁⠈⠉⠄⠄⠄⠄⠄⣤⡄⠄⠄⠄⠄⠄⠈⠄⠈⠻⠿⠛⢿⣿⣿⣿⣿⣿
⢸⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⣠⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣿⣿⣿⣿
⢸⣿⣿⣿⡀⠄⠄⠄⠄⠄⠄⠄⠉⠉⠁⠄⠄⠄⠄⠐⠒⠒⠄⠄⠄⠄⠉⢸⣿⣿⣿
⢸⣿⣿⣿⢿⣦⣄⣠⣄⠛⠟⠃⣀⣀⡀⠄⠄⣀⣀⣀⣀⣀⣀⡀⢀⣰⣦⣼⣿⣿⡿
⢸⣿⣿⣿⣿⣿⣿⣻⣿⠄⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣥⣾⣟⣿⣿⣿⣿⣿
⢸⣿⣿⣿⣿⣿⣿⣿⣿⡆⠈⠿⠿⠿⠿⠿⠿⠿⠿⠿⣧⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""

def price():
    print('\nFancy = Over $30\n' 'Normal = $13 - $25\n' 'Cheap = Under $13\n')
    global cost
    flag = True
    while flag == True:
      cost = input("How expensive? [F]ancy, [N]ormal [C]heap: ").upper()
      if cost == 'F' or 'N' or 'C':
        break
      else:
        print('\nInvalid Input (Choose between F, N, or C)\n ')
        continue      

def cuisine():
    global type_of_food  
    type_of_food = input("\nWhich Cuisine? ").upper()

cheap_american = ('McD', 'Wendy\'s', 'A&W', 'Carl\'s Jr', 'Burger King KEKW')

initialize = input()
if initialize == ".":
  price()
  cuisine()

if type_of_food == 'KOREAN':
  if cost =='C':
    print('Daniel\'s House')
  elif cost == 'N':
    print('Nadri')
  elif cost == 'F':  
    print('Kook KBBQ')

if type_of_food == 'AMERICAN':
  if cost =='C':
    print(random.choice(cheap_american))
  elif cost == 'N':
    print('Cactus Club')
  elif cost == 'F':  
    print('Hy\'s Steakhouse')

if type_of_food == 'JAPANESE':
  if cost == 'C':
    print('idk')
  elif (type_of_food == 'JAPANESE') and (cost == 'N'):
    print('somewhere')
  elif (type_of_food == 'JAPANESE') and (cost == 'F'):  
    print('Masayoshi')