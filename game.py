# ____________________________________________________________________    # MAIN MENU
while True: # while true helps with user input validation
    print("Main Menu")      # main menu prompt 
    print("\n1. Start Game")
    print("2. Exit game")

    while True:  
        try:
            user_choice = int(input("\nChoose: "))

            if user_choice == 1:
                print("\nGame starting!")         # allows user to either leave or start game
                break
    
            elif user_choice == 2:
                print("\nSee you next time! ")
                exit()
    
            else:
                print("\nPlease choose an option. ")
        
        except ValueError: 
            print("\nInvalid response, please enter a number") 
            continue
    break
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
            print("\nInvalid response, please enter a number. ")
            continue
    
        break

    print("\nWelcome, " + player_name + " the " + player_class + "!")   # welcomes player with name and class

# _____________________________________________________________________   # FIRST STORY LOCATION

def location1_hangerbay():
    global health, inventory

    print("\nYou spawn in location 1, Hanger Bay.")
    print("\nThe ship's hangar is smoky and dark. Emergency lights flicker.")
    print("\nAn escape pod sits in the distance, but the door is locked.")

    print("\nYou go to the escape pod. ")
    print("\nYour crewmate asks for a favor: Help me clean the trash. ")

    while True:
            user_choice = input("Help him? (yes/no): ")   # asks for player's choice

            if user_choice == "yes":
                print("\nHe gives you an unknown key ")      # adds key to inventory
                inventory.append("Mysterious_Key")
                break
                
            elif user_choice == "no":
                print("\nYou ignore him, and continue by yourself ")

                break
                
            else:
                print("\nPlease answer yes or no")



    print("\nA fire blocks your path! ")
    print("\n1. Run through and risk taking damage ")
    print("\n2. Find another method ")



    
    while True:
        try:
            user_choice2 = int(input("\nChoose (1-2): "))
            
            if user_choice2 == 1:
                health = health - 20
                print("\nYou took 20 damage... Health: " , health)   # lowers player's health
                break

            
            elif user_choice2 == 2:
                if "Mysterious_Key" in inventory:
                    print("\nYou open an unknown door and escape the pod!! ")
                    break
                    
                else:
                    print("\nYou are trapped...you died")
                
            else:
                print("\nPlease choose an option")

        except ValueError:
            print("\nInvalid response, please enter a number")
            continue

        
# _____________________________________________________________________ # PATH SELECTING


       
    
    










# _____________________________________________________________________  # function testing
         
create_player()

show_stats()

location1_hangerbay()



    

