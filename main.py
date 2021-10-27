class decisions():
    def price(self):
        print('\nFancy = Over $30\n'
              'Normal = $13 - $25\n'
              'Cheap = Under $13\n')
        self.cost = input("How expensive? [F]ancy, [N]ormal [C]heap ").upper()
        if self.cost == 'F':
            print('\nHy\'s Steakhouse\n')
        elif self.cost == 'N':
            print('cactus club cafe\n')
        else:
            print('\ntaco bell\n')

    def cuisine(self):
        self.type_of_food = input("Which Cuisine? ").upper()
        if (self.type_of_food == 'KOREAN') and (cost == 'C'):
            print('Daniel\'s House')


d = decisions()

initialize = input()
if initialize == ".":
    d.price()
    d.cuisine()
