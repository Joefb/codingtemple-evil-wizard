import random
import os
import classes
from classes import Warrior, Mob, Char, Items

# new_toon = classes.Warrior("bob")
# new_mob = classes.Mob("goblin")
new_toon = Warrior("bob")
new_mob = Mob("goblin")


#### TESTING AREA CODE #######
# new_toon = Warrior("bob")
# new_mob = Mob("goblin")

print(f"You encounter a {new_mob.name}!")
input("Press enter to continue...")
print("")

while new_toon.health > 0 and new_mob.health > 0:
    print("--------- Toon Status ---------")
    print(f"{new_toon.name} Health: {new_toon.health}")
    print(f"{new_mob.name} Health: {new_mob.health}")
    print(f"Attack Power: {new_toon.atk_power}")
    print(f"Armor Class: {new_toon.armor_class}")
    print(f"Weapon: {new_toon.weapon_name}")
    print(f"weapon Damage: {new_toon.weapon_damage}")
    print(f"Enrage Counter: {new_toon.enrage_cooldown}")
    print(f"Inventory: {new_toon.inventory}")
    print("---------------------------")
    print("")
    print("--------- Mob Status ---------")
    print(f"{new_mob.name} Health: {new_mob.health}")
    print(f"Attack Power: {new_mob.atk_power}")
    print(f"Armor Class: {new_mob.armor_class}")
    print(f"Weapon: {new_mob.weapon_name}")
    print(f"weapon Damage: {new_mob.weapon_damage}")
    #
    #     ## Attack and check if mob or player is stuned or dead
    new_toon.do_action(new_mob.name, new_mob.armor_class, new_toon.atk_power)
    if new_mob.health <= 0:
        print(f"You have defeated the {new_mob.name}!")
        new_toon.loot_mob(new_mob)
        print(f"Inventory: {new_toon.inventory}")
        break

    new_mob.do_action(new_toon.name, new_toon.armor_class, new_mob.atk_power)
    if new_toon.health <= 0:
        print("You have been defeated!")
        break
