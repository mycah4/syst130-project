# ____________________________________________________________________    # MAIN MENU
while True:
    print("Main Menu")      # main menu prompt 
    print("\n1. Start Game")
    print("2. Exit game")

    user_choice = input("\nChoose: ")

    if user_choice == "1":
        print("\nGame starting!")         # allows user to either leave or start game
        break
    
    elif user_choice == "2":
        print("\nSee you next time! ")
        break
    
    else:
        print("\nNo choice found ")
# ____________________________________________________________________  # STARTER STATS
story_level = 1     # global variables
health = 100
inventory = []
player_name = ""
player_class = ""
# _____________________________________________________________________   # PLAYER CREATION

def show_stats():
    print("\nStory Level:", story_level)    # function to display stats
    print("\nHealth:", health)
    print("\nInventory:", inventory)

def create_player():
    global player_name, player_class, health   # function for character creation

    player_name = input("\nChoose a name for your character: ") # gets player name

    print("\nChoose your class!") # chooses player class
    print("\n1. Soldier (+30 health)")
    print("\n2. Engineer (Auto-solves puzzles)")
    print("\n3. Medic (Gain health after every fight)")

    user_choice = input("\nChoose (1-3): ")

    if user_choice == "1":
        player_class = "Soldier"
        health = health + 30
        
    elif user_choice == "2":
        player_class = "Engineer"
        
    else:
        player_class = "Medic"

    print("\nWelcome, " + player_name + " the " + player_class + "!")   # welcomes player with name and class

# _____________________________________________________________________   # FIRST STORY PATH

def path1_escapepod():
    global health

    print("\nYou go to the escape pods. ")
    print("\nYour crewmate asks for a favor: Help me clean the trash. ")

    user_choice = input("Help him? (yes/no): ")   # asks for player's choice

    if user_choice == "yes":
        print("\nHe gives you an unknown key ")      # adds key to inventory
        inventory.append("Mysterious_Key")

    else:
        print("\nYou ignore him, and continue by yourself ")

    print("\nA fire blocks your path! ")
    print("\n1. Run through and risk taking damage ")
    print("\n2. Find another method ")

    user_choice2 = input("Choose (1-2): ")

    if user_choice2 == "1":
        health = health - 20
        print("\nYou took 20 damage... Health: " , health)   # lowers player's health

    elif "Mysterious_Key" in inventory:
        print("\nYou open an unknown door and escape the pod!! ")
        return True

    else:
        print("\nThe door is locked, you can't escape the pod leading to your death! ")
        return False

# _____________________________________________________________________  # function testing
         
create_player()

show_stats()

path1_escapepod()



    

