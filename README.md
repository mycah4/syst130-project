# Adventure to Space Game by Mycah Eccles|


## How to run the game
1. Have python 3.x installed on your system
2. Download all files "game.py", "player.py", "locations.py", "save_load.py", "audit.py"
3. Run the game from command prompt:
   '''bash
   python game.py


**GAME DESCRIPTION:**

**3 Story paths:**
Path 1: The Bridge - The player goes to the ship's command bridge to hack the main computer. Captain Voss's hologram presents a riddle that must be solved to obtain the Keycard and Launch Code.

Path 2: The Medical Bay - The player visits the medical bay where injured crew members are located. They receive a Medkit and meet Ensign Riley who provides the Launch Code and Keycard.

Path 3: The Engine Room - The player helps Engineer Takeda in the overheating engine room. They face a gas vent explosion challenge and receive the Launch Code.

3 Endings:
Best Ending - The player has BOTH the Keycard AND Launch Code when reaching the escape pod. The computer authorizes launch and the player escapes successfully.

Average Ending - The player has ONLY ONE of the required items (Keycard OR Launch Code). Launch is denied and the ship explodes, but the player survives.

Worst Ending - The player has NEITHER the Keycard nor Launch Code. Launch is denied and the player dies in the explosion.

**5 Locations & Events**
Hangar Bay - Starting location where the player wakes up. A crewmate asks for help cleaning trash, offering a Mysterious Key. Fire blocks the path requiring a choice between taking damage or finding another way.

The Bridge - Command center with Captain Voss's hologram. Player must solve a riddle to get the Keycard and Launch Code.

Medical Bay - Triage area with injured crew. Player receives a Medkit and meets Ensign Riley who provides important items.

Engine Room - Overheating reactor room with Engineer Takeda. Player faces a gas vent explosion challenge.

Escape Pod Bay - Final location where the player attempts to launch the escape pod. Ending depends on collected items.

**NPCS:**

NPC 1: Crewmate

Where they appear: Hangar Bay

What they do: Asks player to help clean trash. Gives Mysterious Key if player says "yes". Refusing means no key for later puzzles.

NPC 2: Captain Voss (Hologram)

Where they appear: The Bridge

What they do: Presents a riddle that must be solved. Gives Keycard and Launch Code for correct answer. Shocks player for wrong answers (damage).

NPC 3: Doctor

Where they appear: Medical Bay

What they do: Waves player over frantically. Gives Medkit item for healing. Explains Medkit mechanics.

NPC 4: Ensign Riley

Where they appear: Medical Bay

What they do: Injured crew member asking for help. Provides Launch Code. Explains about Keycard location.

NPC 5: Engineer Takeda

Where they appear: Engine Room

What they do: Shouts about melting reactor. Needs conductive metal (Mysterious Key). Can help seal gas vent if player has Conductive Rod.

**5 Inventory Items:**

Item 1: Mysterious Key

Where obtained: Hangar Bay by helping crewmate

What it is used for: Used to bypass fire in Hangar Bay. Can be melted into Conductive Rod in Engine Room.

Item 2: Medkit

Where obtained: Medical Bay from doctor

What it is used for: Heals +30 health (+60 for Medic class). Can be used immediately or saved.

Item 3: Keycard

Where obtained: Bridge (solving riddle) or Medical Bay (finding bodies)

What it is used for: Required for best ending. Used with Launch Code to escape.

Item 4: Launch Code

Where obtained: Bridge, Medical Bay, or Engine Room (code "734")

What it is used for: Required for best ending. Used with Keycard to authorize launch.

Item 5: Conductive Rod

Where obtained: Engine Room by melting Mysterious Key

What it is used for: Used to seal gas vent during explosion. Saves player from damage in challenge.

**2 Challenges**

Challenge 1: Captain's Riddle

Where it occurs: Location 2 - The Bridge

What the player must do: Answer two riddles correctly

First riddle: "What has keys but no locks, space but no room, a face but no eyes?" Answer: keyboard

Second riddle (if needed): "I have a head and a tail" Answer: coin

What happens on success: Receive Keycard and Launch Code, continue game

What happens on failure: Take 15 damage, second chance given; if both fail, game over

### Challenge 2: Gas Vent Explosion

Where it occurs: Location 4 - Engine Room

What the player must do: Choose where to hide from explosion in 3 seconds

Option 1: Hide behind coolant tank

Option 2: Run through gas to exit

Option 3: Call for Engineer Takeda's help

What happens on success: Option 1 = no damage, Option 3 = no damage if have Conductive Rod

What happens on failure: Takes 25-40 damage depending on choice; death if health reaches 0

## Cyber Pack Features

### Feature 1: Input Validation + Safe Error Handling

All user inputs use try/except blocks to catch ValueError exceptions. Menu choices re-prompt on invalid input. String inputs use .lower() to handle case variations. The game never crashes from unexpected input types.

### Feature 2: Audit Logging (audit_log.txt)

Every security event is logged with timestamp. Logs include: SAVE, LOAD, TAMPER_DETECTED, CREATE, DEATH, WIN, LOSS. Format is [YYYY-MM-DD HH:MM:SS] EVENT_TYPE: details. Example: [2024-01-15 14:30:25] TAMPER_DETECTED: Save file hash mismatch

### Feature 3: Save/Load with Tamper Check

Save process: Game state saved as JSON with SHA256 hash. The hash acts as a fingerprint of the save data.

Load process: When loading, the hash is recalculated from the saved data and compared to the stored hash.

Tamper detection: If the hashes do not match, the save file has been modified. The game rejects the save and starts a new game instead.

Security benefit: Prevents players from cheating by editing health or inventory values in the save file.

## File Structure

syst130-project/
├── game.py          # Main game loop and menu
├── player.py        # Player stats and creation
├── locations.py     # All 5 locations and challenges
├── save_load.py     # Save/load with SHA256 tamper check
├── audit.py         # Audit logging functions
├── savegame.json    # Auto-generated save file
└── audit_log.txt    # Auto-generated security log

## Version

v1.0 - Final Submission
