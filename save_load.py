import hashlib
import json
import os
from audit import create_audit_log

def save_game(health, inventory, player_name, player_class):       # save game with JSON and SHA256 hash for temper detection


    game_data = {             # dictionary for game data
        "health": health,
        "inventory": inventory,
        "player_name": player_name,
        "player_class": player_class,
        }

    
    json_data = json.dumps(game_data) # makes dictionary into a JSON string

    game_hash = hashlib.sha256(json_data.encode()).hexdigest()  # creates sha256 of json string

    with open("savegame.json", "w") as f:
        json.dump({"hash": game_hash, "data": game_data}, f, indent=2}) # saves hash and json to a file

    print("Game saved with tamper protection")
    create_audit_log("SAVE", f"Game saved. Health: {health")

def load_game(): # loads game and checks if it has been tampered

    if not os.path.exists("savegame.json"): # checks if save file exists
        print("\nNo save file found. Starting new game.")
        return None

    try:
        with open("savegame.json", "r") as f: # reads save file
            save_data = json.load(f)

        stored_hash = save_data["hash"]  # grabs the stored hash and game data
        game_data = save_data["data"]

        json_data = json.dumps(game_data) #recalculates hash from the game data
        calculated_hash = hashlib.sha256(json_data.encode()).hexdigest()

        if stored_hash != calculated_hash:  # if stored hash doesn't equal the new hash, file has been tampered
            print("\nFile has been tampered!")
            print("\nYour save file has been modified")
            print("\nYour safe file is rejected for security reasons")
            print("\nStarting a new game instead.")
            create_audit_log("TAMPER_DETECTED", "Save file hash mismatch")
            return None    

        print("\nGame loaded successfully") # not tampered
        create_audit_log("LOAD", f"Game loaded. Health: {game_data['health']}")
        print("\nNo tampering detected!")
        return game_data

    except FileNotFoundError: # if no file found starts a new game
        print("No save file found. Starting a new game.")
        return None

    except json.JSONDecodeError: # if json error starts a new game
        print("Save file error. Starting a new game")
        return None


