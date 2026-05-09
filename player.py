from audit import create_audit_log

# ____________________________________________________________________  # STARTER STATS    
health = 100
inventory = []
player_name = ""
player_class = ""

# ____________________________________________________________________  #r PLAYER CREATION

def show_stats():    # function to display stats
    print("\nHealth:", health)
    print("\nInventory:", inventory)

def create_player():
    global player_name, player_class, health   # function for character creation

    player_name = input("\nChoose a name for your character: ") # gets player name

    print("\nChoose your class!") # chooses player class
    print("\n1. Soldier (+30 health)")
    print("\n2. Engineer (Auto-solves puzzles)")
    print("\n3. Medic (Medkit heals more)")
    
    while True:
        try:
            user_choice = int(input("\nChoose (1-3): "))

            if user_choice == 1:
                player_class = "Soldier"
                health = health + 30
        
            elif user_choice == 2:
                player_class = "Engineer"
        
            elif user_choice == 3:
                player_class = "Medic"

            else:
                print("\nPlease choose a response")

        except ValueError:
            print("\nInvalid response, please enter a number. ") # makes sure data type is correct
            continue
    
        break

    print("\nWelcome, " + player_name + " the " + player_class + "!")   # welcomes player with name and class


# _____________________________________________________________________   # HEALTH CHECK
def check_death(): # checks if player health is 0
    global health
    
    if health <= 0:
        print("You have died...")
        exit()
    
