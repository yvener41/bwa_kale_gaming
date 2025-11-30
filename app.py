import random
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# -------------------------------
# PLAYER & ENEMY STATS
# -------------------------------

player = {
    "name": "",
    "hp": 25,
    "attack": 5,
    "defense": 2,
    "potions": 3,
    "gold": 0
}

def create_enemy(stage):
    if stage == 1:
        return {"name": "Goblin Scout", "hp": 12, "attack": 3}
    elif stage == 2:
        return {"name": "Cave Troll", "hp": 18, "attack": 4}
    elif stage == 3:
        return {"name": "Shadow Wraith (BOSS)", "hp": 30, "attack": 6}

# -------------------------------
# BATTLE FUNCTION
# -------------------------------

def battle(enemy):
    slow_print(f"\n⚔️ A wild {enemy['name']} appears!")
    
    while enemy["hp"] > 0 and player["hp"] > 0:
        print(f"\nYour HP: {player['hp']} | Enemy HP: {enemy['hp']}")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Potion")
        print("4. Attempt Escape")

        move = input("\nChoose your action: ")
        
        # --- Attack ---
        if move == "1":
            dmg = random.randint(player["attack"]-1, player["attack"]+2)
            crit = random.random() < 0.2  # 20% crit chance

            if crit:
                dmg *= 2
                slow_print("💥 CRITICAL HIT!")

            enemy["hp"] -= dmg
            slow_print(f"You struck the {enemy['name']} for {dmg} damage!")

        # --- Defend ---
        elif move == "2":
            slow_print("🛡️ You brace for the attack! Damage reduced.")
            dmg = max(0, enemy["attack"] - player["defense"])
            player["hp"] -= dmg
            slow_print(f"The enemy hits you for {dmg} reduced damage.")
            continue

        # --- Potion ---
        elif move == "3":
            if player["potions"] > 0:
                heal = random.randint(6, 10)
                player["hp"] += heal
                player["potions"] -= 1
                slow_print(f"🧪 You healed {heal} HP. Potions left: {player['potions']}")
            else:
                slow_print("❌ No potions left!")
                continue

        # --- Escape ---
        elif move == "4":
            if random.random() < 0.4:
                slow_print("🏃 You managed to escape!")
                return True
            else:
                slow_print("❌ You failed to escape!")
        else:
            slow_print("Invalid choice!")
            continue

        # --- Enemy Turn ---
        if enemy["hp"] > 0:
            dmg = random.randint(enemy["attack"]-1, enemy["attack"]+1)
            player["hp"] -= dmg
            slow_print(f"💥 The {enemy['name']} hits you for {dmg} damage!")

    # Battle result
    if player["hp"] <= 0:
        slow_print("\n💀 You have been defeated...")
        return False
    else:
        slow_print(f"\n🎉 You defeated the {enemy['name']}!")
        gained_gold = random.randint(5, 12)
        player["gold"] += gained_gold
        slow_print(f"You found {gained_gold} gold!")
        return True

# -------------------------------
# GAME INTRO
# -------------------------------

def intro():
    slow_print("Welcome to the Cavern of Shadows RPG!")
    player["name"] = input("What is your hero's name? ")
    slow_print(f"\nGreetings, {player['name']}... your adventure begins.")
    time.sleep(1)

# -------------------------------
# MAIN GAME STORY
# -------------------------------

def game():
    intro()

    slow_print("\nYou stand at the entrance of the Cavern of Shadows...")
    slow_print("Legends say a cursed treasure lies deep within.")
    slow_print("Only the bravest adventurers return alive.\n")

    choices = ["left", "right"]

    # First decision
    choice = input("Do you go LEFT or RIGHT? ").lower()

    if choice not in choices:
        slow_print("You hesitate too long... and a goblin ambushes you!")
        if not battle(create_enemy(1)):
            return

    # LEFT PATH
    if choice == "left":
        slow_print("\nThe left tunnel glows faintly with blue crystals.")
        slow_print("You feel a cool breeze... something is watching you.")
        if not battle(create_enemy(1)):
            return

        slow_print("\nAfter defeating the goblin, you find a potion!")
        player["potions"] += 1

    # RIGHT PATH
    else:
        slow_print("\nYou walk down a dark narrowing tunnel.")
        slow_print("Suddenly — a massive Cave Troll blocks your path!")
        if not battle(create_enemy(2)):
            return

    # BOSS BATTLE
    slow_print("\nYou reach the final chamber...")
    slow_print("A dark mist swirls into shape...")
    slow_print("🔥 THE SHADOW WRAITH APPEARS! 🔥")

    if not battle(create_enemy(3)):
        return

    # ENDING
    slow_print("\n🏆 You have conquered the Cavern of Shadows!")
    slow_print(f"Final Stats — HP: {player['hp']} | Gold: {player['gold']} | Potions: {player['potions']}")
    slow_print("\nYou are now a legend among adventurers!")
    slow_print("\nTHE END\n")

# -------------------------------
# PLAY AGAIN LOOP
# -------------------------------

while True:
    game()
    retry = input("\nPlay again? (y/n): ").lower()
    if retry != "y":
        slow_print("Thanks for playing! Goodbye.")
        break
    else:
        # Reset player stats for new run
        player["hp"] = 25
        player["potions"] = 3
        player["gold"] = 0
