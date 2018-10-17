
# Get current day for starting date
from datetime import datetime
now = datetime.now()

# Globals
import variables

# Cage Days
def cage_day():
    print("\nIt is currently %s %s %s.\
    \n ____________________________\n" % (now.day, now.strftime("%B"), now.year))
    print("%s has 2 days before they have to take off. \
    \n%s takes one last look at their cage." % (variables.bun_name, variables.bun_name))
    choice_one = input ("\nThere is: \
    \n(1) A piece of lettuce \
    \n(2) A pebble\
    \n\nWhich do they take? (1/2)")

    if choice_one == '1' :
        empty_index = variables.inventory.index("empty")
        variables.inventory[empty_index] = "lettuce"
        print("%s grabbed a piece of %s. \
        \nThis might be useful later." % (variables.bun_name, variables.inventory[empty_index]))
        variables.pebble_lettuce = False

    elif choice_one == '2' :
        empty_index = variables.inventory.index("empty")
        variables.inventory[empty_index] = "pebble"
        print("%s grabbed a %s. \
        \nThis will be useful later." % (variables.bun_name, variables.inventory[empty_index]))

    else :
        print("\nThis is a simple game with simple rules. \
               \nLet\'s try this again.\n")
        cage_day()

def pebble_cat():
    print("\n____________________________\nThe cat walks into the room and makes eye contact with you.")
    variables.pebble_cat_choice = input ("Do you want to throw the pebble?\n(yes/no)")

def lettuce_cat():
    print("\n____________________________\nThe cat walks into the room and makes eye contact with you.")
    variables.lettuce_cat_choice = input("Do you want to throw the lettuce?\n(yes/no)")

def cat():
    if "pebble" in variables.inventory:
        pebble_cat()
    else:
        lettuce_cat()

