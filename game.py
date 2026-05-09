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

def location1_hangarbay():
    global health, inventory

    print("\nYou spawn in location 1, Hangar Bay.")
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
            print("\nInvalid response, please enter a number")
            continue
    
# _____________________________________________________________________ # SECOND STORY LOCATION (path 1)
    
def location2_bridge():
    global health, inventory


    print("\nYou are now in location 2, the Bridge.")
    print("\nYou enter the ship's command bridge. Sparks fly from broken consoles.")                    # storyline, path 1, npc 1
    print("\nCaptain Voss is slumped over her terminal. A hologram flickers to life.")
    print("\nThe captain's hologram appears, 'I've locked the escape. Solve my riddle first!'")

    print("\nChallenge #1... the Captain's riddle")    #storyline, challenge 1
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

def location3_medicalbay():
    global health, inventory, player_name


    print("\nYou are now in location 3, the Medical Bay") # storyline, path 2, npc 2
    print("\nThe medical bay is trashed. Injured crew members lie on cots.")                    
    print("\nA doctor waves you over frantically")
    print("\nYou made it out successfully... take this medkit it'll help you!") # player receives medkit
    inventory.append("Medkit")

    print("You gained a medkit! It gives +30 health when used.")

    while True:
        use = input("Do you want to use the medkit?(yes/no)") # asks for player input to use medkit

        if use == "yes":
            health = health + 30
            inventory.remove("Medkit")   # removes medkit
            print("\nYou're health increased to ", health)

        elif use == "no":
            print("\nYou decided to save it for later") # stays in inventory

        else:
            print("\nPlease answer yes or no")

    print("\nAn unknown figure approaches you")  # storyline
    print("\nHello, I am Ensign Riley... The captain left her keycard behind on the bridge. I'm injured, can you find it?")
    print("\nBefore you leave this might be important to you!")
    print("\nHe gives you the launch code.")

    if "Launch_Code" not in inventory:  # checks if launch code previously exists, if not you receive it
        inventory.append("Launch_Code") 

    print("\nYou search the bodies. You find a keycard!") 
    if "Captain_Keycard" not in inventory: # checks if the keycard previously exists, if not you receive it
        inventory.append("Captain_Keycard")

    print("\nThe medical bay cleared, you have what you need.")
    return True
    
# _____________________________________________________________________ # FOURTH STORY LOCATION (path 3)

def location4_engineroom():
    global health, inventory 
    
    print("\nYou are now in location 4, the engine room") # storyline, path 3, npc 3
    print("\nThe engine room is overheating. Alarms blare. Coolant leaks everywhere.")                    
    print("\nEngineer Takeda shouts: The reactor is melting!")
    print("\nEngineer Takeda says: I need a conductive metal... Do you have any?") 

    if "Mysterious_Key" in inventory:   # checks for key
        print("\nYou show Takeda the Mysterious Key")
        print("\nHe gracefully accepts it and melts it into a conductive rod")
        inventory.remove("Mysterious_Key")    # removes key, adds rod
        inventory.append("Conductive_Rod")
        print("\nYou received a conductive rod!")
              
    else:
        print("\nEngineer Takeda says: You have no key? Unfortunately you'll have to risk the gas vent..")

    print("\nChallenge #2: Gas Vent Explosion") # storyline, challenge 2
    print("\nYou have three seconds to choose where to hide!")

    print("\n1. Hide behind the cooplant tank") 
    print("\n2. Run through the gas to the exist")
    print("\n3. Call for Engineer Takeda's help")

    while True:
        try:
            choice = int(input("\nChoose (1-3): ")) # user input to pick where to hide

            if choice == 1:
                print("\n The coolant tank absorbs the heat! You took no damage!") 
                break

            elif choice == 2:
                health = health - 40
                print("You run through the gas and take damage. Health: ", health) # -40 health from gas
                break

            elif choice == 3:
                if "Conductive_Rod" in inventory:                # looks for rod to seal the vent
                    print("\nTakeda uses the rod to seal the vent!")
                          
                else:
                    health = health - 25             #-25 from gas
                    print("\nTakeda is too slow and you take damage. Health:", health)
                
                break

            else:
                print("\nPlease choose 1, 2 or 3")

        except ValueError:
            print("\nInvalid response, please enter a number")
            continue

    print("\nYou make it through the engine room")


    if "Launch_Code" not in inventory:     #checks if launch_code exists, if not adds it
        print("Takeda says: Here's the launch code I found it. It's 734.")
        inventory.append("Launch_Code")\

    return True
    


# _____________________________________________________________________ # LAST STORY LOCATION 


def location5_escapepodbay():
    global health, inventory
    
    print("\nYou are now in location 5, the Escape Pod Bay")
    print("\nYou reach the escape pod bay. Only one pod remains.")                   
    
    print("\nYou approach the pod's computer.")
    while True:
        try:
            if "Captain_Keycard" in inventory and "Launch_Code" in inventory:
                print("\n Computer: Keycard detected. Launch code accepted.")   # best ending if player has keycard and launch code
                print("\n Best Ending! You escaped successfully")
                return True


            
            elif "Captain_Keycard" in inventory or "Launch_Code" in inventory:  # second best ending if player has one or the other
                print("\nComputer: Missing authorization. Launch requires both keycard")
                print("\nThe alarms get louder. The ship explodes")
                print("\nAverage Ending! You made it to the end but didn't escape....")
                return False
                
            else:
                print("\nComputer: No authorization detected. Launch denied")  # worst ending, if player doesn't have either
                print("\nThe ship explodes. You don't escape")
                print("\nThe worst ending! You didn't have any authorization")
                return False
    
# _____________________________________________________________________  # MAIN GAME
         
def start_game():
    global health, inventory   


    create_player()    
    show_stats()

    location1_hangarbay()

    path = choose_path()


    if path == 1:
        print("\n You take the path to the bridge...")

        if not location2_bridge():
            print("\nGame over... failed bridge puzzle")
            return

    elif path == 2:
        print("\nYou take the path to the medical bay...")
        if not location3_medicalbay():
            print("\nGame over.. Medical Bay was a trap!")
            return

    elif path == 3:
        print("\nYou take the path to the engine room..."
        if not location4_engineroom():
            print("\nGame over... the engine room exploded") 
            return

    print("\nThe speaker: SELF DESTRUCTION IN 60 SECONDS!") 
    location5_escapepodbay()

    print("\nYour final stats! ") # prints final stats
    show_stats()

# _____________________________________________________________________  # function          

start_game()

    

