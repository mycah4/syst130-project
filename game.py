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

    player_name = input("Choose a name for your character")
    
    

