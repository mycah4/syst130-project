import player
import locations
from audit iomport create_audit_log
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

# _____________________________________________________________________  # function          

start_game()

    

