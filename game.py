# ____________________________________________________________________    # MAIN MENU
while True:
    print("\n Main Menu")      # main menu prompt 
    print("1. Start Game")
    print("2. Exit game:")

    user_choice = input("Choose: ")

    if user_choice == "1":
        print("Game starting!")         # allows user to either leave or start game
        break
    
    elif user_choice == "2":
        print("See you next time!")
        break
    
    else:
        print("No choice found")
# ____________________________________________________________________  # STARTER STATS
story_level = 1     # global variables
health = 100
inventory = []
player_name = ""
player_class = ""
# _____________________________________________________________________   # PLAYER CREATION

def show_stats():
    print("Story Level:", story_level)    # function to display stats
    print("Health:", health)
    print("Inventory:", inventory)

def create_player():
    global player_name, player_class, health   # function for character creation

    player_name = input("Choose a name for your character") # gets player name

    print("Choose your class!") # chooses player class
    print("1. Soldier (+30 health)")
    print("2. Engineer (Auto-solves puzzles)")
    print("3. Medic (Gain health after every fight)")

    user_choice = input("Choose (1-3): ")

    if user_choice == "1":
        player_type = "Soldier"
        health = health + 30
        
    elif user_choice == "2":
        player_type = "Engineer"
        
    else:
        player_type = "Medic"

    print("Welcome, " + player_name + "the " + player_class + " !")   # welcomes player with name and class

# _____________________________________________________________________   # FIRST STORY PATH


def path1_escapepod():

    print("You go to the escape pods.")
    print("Your crewmate asks for a favor: Help me clean the trash.")

    user_choice = input("Help him? (YES/NO): ")   # asks for player's choice

    if user_choice == "yes":
        print("He gives you an unknown key")      # adds key to inventory
        inventory.append("Mysterious_Key")

    else:
        print("You ignore him, and continue by yourself")

    print("A fire blocks your path!")
    print("1. Run through and risk taking damage")
    print("2. Find another method")

    user_choice2 = input("Choose (1-2): ")

    if user_choice2 == "1":
        health = health - 20
        print("You took 20 damage... Health: " + health)   # lowers player's health

    if "Mysterious_Key" in inventory:
        print("You open an unknown door and escape the pod!!")
        return true

    else:
        print("The door is locked, you can't escape the pod")
        return false

# _____________________________________________________________________  # function testing
         
create_player()

show_stats()

path1_escapepod()



    

