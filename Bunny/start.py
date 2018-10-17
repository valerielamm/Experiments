
# Globals
import variables

# Intro
def introductions():
    print("\n\nBunny Tales: The Golden Carrot\
        \nThere once was a bunny that was trapped in a cage.\
        \nHis owner used to feed him all kinds of treats. \
        \nHe used to get carrots, kale, broccoli, and sweet\
        \ngrasses. One day his owner stopped bringing him\
        \nall the tasty foods. All he got was lettuce.\
        \nHe spent every day mindlessly eating the tasteless\
        \nlettuce. Every night, he dreamt of the tale of the\
        \ngolden carrot...\n\n／(･ × ･)＼\n")


# Ask user if they want to play
def play():

    enter_game = input ("Do you want to guide the bunny to the golden carrot?\n(yes/no)")

    if enter_game == 'yes' or enter_game == 'Yes'\
            or enter_game == 'YES' or enter_game == 'y'\
            or enter_game == 'Y' :
        variables.bun_name = input ("\nName your bunny: ")
    elif enter_game == 'no' or enter_game == 'No'\
            or enter_game == 'NO' or enter_game == 'n' \
            or enter_game == 'N' :
        print("\nThe bunny never gathered the courage to go \
               \nafter the golden carrot. He spent the rest\
               \nof his days sad over what could\'ve been")
        import sys
        sys.exit()
    else:
        print("\nThis is a simple game with simple rules. \
               \nLet\'s try this again.\n")
        play()

def are_you_ready():
    if variables.bun_name == 'name02' :
        print ("...")
    else:
        print("%s is ready to start their journey.\
        \n\n ____________________________" % (variables.bun_name))