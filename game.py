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
    print("\n1. Run through and risk taking damage ")      # pick between two different choices
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
                    exit()
            else:
                print("\nPlease choose an option")

        except ValueError:
            print("\nInvalid response, please enter a number")
            continue

        
# _____________________________________________________________________ # PATH SELECTING

def select_path():
    print("\nYou see a corridor that splits into three seperate directions!")  # function to pick between three paths
    print("\n1. Go to the bridge (Hack the main computer)")
    print("\n2. Go to the medical bay (Find an unknown person with a special keycard)")
    print("\n3. Go to the engine room (Help the engineer!)")

    while True:
        try: 
            user_choice = int(input("\nChoose a path (1-3): ")) # grabs input

            if user_choice == 1:
                return 1

            elif user_choice == 2:
                return

            elif user_choice == 3:
                return
                
            else:
                print("\nPlease choose 1, 2, or 3")

        except ValueError:
            print("\Invalid response, please enter a number")
            continue
    
# _____________________________________________________________________ # SECOND STORY LOCATION (path 1)
    
def location2_bridge():
    global health, inventrory


    print("\nYou are now in location 2, the Bridge.")
    print("\nYou enter the ship's command bridge. Sparks fly from broken consoles.")                    # storyline
    print("\nCaptain Voss is slumped over her terminal. A hologram flickers to life.")
    print("\nThe captain's hologram appears, 'I've locked the escape. Solve my riddle first!'")

    print("\nChallenge #1... the Captain's riddle")
    print("\nWhat has keys but no locks?")
    print("\nHas space but no room?")
    print("\nHas a face but no eyes?")

    answer = input("\nYour answer?: ")  # asks player for input to answer the puzzle

    if answer == "keyboard" or answer == "a keyboard":  # if correct answer you receive two different items
        print("\nCorrect. Take the keycard and my launch code '734'")
        inventory.append("Keycard")
        inventory.append("Launch_Code")
        print("You received the captain's keycard and the launch code!")
        return True

    
    else:
        print("\nYou got the answer wrong, the Captain's Hologram shocks you")  # damages you for wrong answer
        health = health - 15


        while True:
            anotherchance = input("\nTry again? (yes/no): ") # player rceives another chance
            

            if anotherchance == "yes":
                print("\nThis is your last try, I have a head and a tail")
                answer2 = input("What am I?")
                
                if answer2 == "coin" or answer2 == "a coin":            # receives two different item
                    print("Take my keycard and launch code")
                    inventory.append("Keycard")
                    inventory.append("Launch_Code")
                    return true               

                else:
                    print("You failed, the bridge is locking down")       # failed to answer the question correctly
                    return False

            elif second_chance == "no":   # player escapes with nothing
                print("\nYou leave the bridge with nothing...")
                return False
        
            else:
        print("\nPlease answer yes or no")
        


# _____________________________________________________________________ # THIRD STORY LOCATION (path 2)












# _____________________________________________________________________ # FOURTH STORY LOCATION (path 3)


# _____________________________________________________________________ # LAST STORY LOCATION 

# _____________________________________________________________________  # function testing
         
create_player()

show_stats()

location1_hangerbay()



    

