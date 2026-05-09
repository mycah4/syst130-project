import player
import locations
from audit import create_audit_log
from save_load import save_game, load_game
    
# _____________________________________________________________________  # MAIN GAME
         
def start_game():
    print("\nAdventure to escape space!") 

    if saved_data:     # finding and loading saved file
        player.health = sava_data["health"]
        player.inventory = saved_data["inventory"] 
        player.player_name = saved_data["player_name"]
        player.player_class = saved_data["player_class"]
        print("\nWelcome back, {player.player_name}!")
    else:
        player.create_player()

    player.show_stats()


    locations.location1_hangarbay()

    save_choice = input("\nSave game? (yes/no):  ")
    if save_choice == "yes":
        save_game(player.health, player.inventory, player.player_name, player.player_class

    path = locations.select_path()


    if path == 1:
        print("\n You take the path to the bridge...")

        if not locations.location2_bridge():
            print("\nGame over... failed bridge puzzle")
            return 1

    elif path == 2:
        print("\nYou take the path to the medical bay...")
        if not locations.location3_medicalbay():
            print("\nGame over.. Medical Bay was a trap!")
            return 2

    elif path == 3:
        print("\nYou take the path to the engine room...")
        if not locations.location4_engineroom():
            print("\nGame over... the engine room exploded") 
            return 3

    print("\nThe speaker: SELF DESTRUCTION IN 60 SECONDS!") 
    locations.location5_escapepodbay()

    print("\nYour final stats! ") # prints final stats
    player.show_stats()
    create_audit_log("Complete", Game finished")

# _____________________________________________________________________  #  MAIN MENU        

while True: # prompts main menu
    print("\nMain Menu")
    print("\n1. Start New Game")
    print("\n2. Load Game")
    print("\n3. Exit")

    choice = input("\nChoose (1-3): ") # asks user for choice

    if choice == "1": #c reates new game
        create_audit_log("MENU", "Starting new game") 
        start_game()
        break
    elif choice == "2": # loads new game
        create_audit_log("MENU", Loading saved game")
        saved = load_game()
        if saved:
            player.health = saved["health"]
            player.inventory = saved["inventory"]
            player.player_name = saved["player_name"]
            player.player_class = saved["player_class"]
            print(f"\nWelcome back, {player.player_name!")
            locations.location5_escapepodbay()
        break
    elif choice == "3": # exits the game
        print("\nYou exited the game")
        create_audit_log("\nEXIT", "Player quit")
        exit()
    else:
        print("\nInvalid choice. Enter 1, 2, or 3")
          

    

