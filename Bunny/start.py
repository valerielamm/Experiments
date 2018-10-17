# Intro
print("Bunny Tales: The Golden Carrot\n")
print("There once was a bunny that was trapped in a cage.\
       \nHis owner used to feed him all kinds of treats. \
       \nHe used to get carrots, kale, broccoli, and sweet\
       \ngrasses. One day his owner stopped bringing him\
       \nall the tasty foods. All he got was lettuce.\
       \nHe spent every day mindlessly eating the tasteless\
       \nlettuce. Every night, he dreamt of the tale of the \
       \ngolden carrot...\n\n／(･ × ･)＼\n")

# Get current day for starting date
from datetime import datetime
now = datetime.now()

# Globals
bun_name = 'name'
pebble_lettuce = True
inventory = ["empty"]


# Enter Game
def cage_days():
    global pebble_lettuce
    global inventory
    print("\nIt is currently %s %s %s." % (now.day, now.strftime("%B"),now.year))
    print("%s has 2 days before they have to take off. \n\n%s takes one last look at their cage." % (bun_name, bun_name))
    choice_one = input ("There is: \n(1) A piece of lettuce \n(2) A pebble\n\nWhich do they take? (1/2)")

    if choice_one == '1' :
        empty_index = inventory.index("empty")
        inventory[empty_index] = "lettuce"
        print("%s grabbed a piece of %s. \nThis might be useful later." % (bun_name, inventory[empty_index]))
        pebble_lettuce = False

    elif choice_one == '2' :
        empty_index = inventory.index("empty")
        inventory[empty_index] = "pebble"
        print("%s grabbed a %s. This will be useful later." % (bun_name, inventory[empty_index]))

    else :
        print("\nThis is a simple game with simple rules. \
               \nLet\'s try this again.\n")
        cage_days()

# Ask user if they want to play
def enter_loop():
    global bun_name

    enter_game = input ("Do you want to guide the bunny to the \
golden carrot?\n(yes/no)")

    if enter_game == 'yes' or enter_game == 'Yes'\
            or enter_game == 'YES' or enter_game == 'y'\
            or enter_game == 'Y' :
      bun_name = input ("\nName your bunny: ")
      print("%s is ready to start his journey." % (bun_name))
      cage_days()

    elif enter_game == 'no' or enter_game == 'No'\
            or enter_game == 'NO' or enter_game == 'n' \
            or enter_game == 'N' :
        print("\nThe bunny never gathered the courage to go \
               \nafter the golden carrot. He spent the rest\
               \nof his days sad over what could\'ve been")
    else:
        print("\nThis is a simple game with simple rules. \
               \nLet\'s try this again.\n")
        enter_loop()

enter_loop()
