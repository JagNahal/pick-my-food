def price():
    print('\nFancy = Over $30\n' 'Normal = $15 - $30\n' 'Cheap = Under $15\n')
    flag = True
    while flag == True:
        cost = input("How expensive? [F]ancy, [N]ormal [C]heap: ").upper()
        if (cost == 'F') or (cost == 'N') or (cost == 'C'):
            break
        else:
            print('\nInvalid Input (Choose between F, N, or C)\n ')
            continue
    return cost


def cuisine():
    cuisine_type = input("\nWhich Cuisine? ").upper()
    return cuisine_type

def dish():
  dish_type = input('\nSpecific Dish In Mind? ')
  return dish_type
