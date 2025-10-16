import random
import os
import classes


class Game:
    def __init__(self, player, mob):
        self.player = player
        self.mob = mob

    def battle(self, player, mob):
        """
        Handles battle loop
        """
        # clear the console
        os.system("cls" if os.name == "nt" else "clear")
        print(f"You encounter a {mob.name}!")
        input("Press enter to continue...")
        print("")

        # self.display_status(player, mob)
        counter = 1
        # while True:
        while player.health > 0 and mob.health > 0:
            try:
                print("What will you do?")
                print("Choose a action:")
                for skill in player.actions:
                    print(f"{counter}) {skill}")
                    counter += 1

                # gets player action
                action = int(input("-> "))
                if action < 1 or action > len(player.actions):
                    counter = 1
                    print("Invalid input. Please enter a action number.")
                    continue

            except ValueError:
                counter = 1
                print("Invalid input. Please enter a action number.")

                # else:
                # continue

            # while player.health > 0 and mob.health > 0:
            # os.system("cls" if os.name == "nt" else "clear")
            # self.display_status(player, mob)
            print("")
            counter = 1
            player_action_result = str(player.do_action(action, mob))
            # mob_action_result = str(mob.do_action(action, player))
            if mob.health <= 0:
                print(f"You have defeated the {mob.name}!")
                player.loot_mob(mob)
                print(f"Inventory: {player.inventory}")
                return
                # break

            # mob.do_action(player)
            _action = None
            mob_action_result = str(mob.do_action(_action, player))
            if player.health <= 0:
                print("You have been defeated!")
                return
                # break

            # prints the player damage
            print(player_action_result)
            print(mob_action_result)

    def display_status(self, player, mob):
        print("--------- Toon Status ---------")
        print(f"{new_toon.name} Health: {new_toon.health}")
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
        print(f"Inventory: {new_mob.inventory}")


#### TESTING AREA CODE #######
new_toon = classes.Warrior("bob")
new_mob = classes.Mob("goblin")
game = Game(new_toon, new_mob)
game.battle(new_toon, new_mob)
# new_toon = Warrior("bob")
# new_mob = Mob("goblin")

# print(f"You encounter a {new_mob.name}!")
# # input("Press enter to continue...")
# print("")
#
# while new_toon.health > 0 and new_mob.health > 0:
#     print("--------- Toon Status ---------")
#     print(f"{new_toon.name} Health: {new_toon.health}")
#     print(f"Attack Power: {new_toon.atk_power}")
#     print(f"Armor Class: {new_toon.armor_class}")
#     print(f"Weapon: {new_toon.weapon_name}")
#     print(f"weapon Damage: {new_toon.weapon_damage}")
#     print(f"Enrage Counter: {new_toon.enrage_cooldown}")
#     print(f"Inventory: {new_toon.inventory}")
#     print("---------------------------")
#     print("")
#     print("--------- Mob Status ---------")
#     print(f"{new_mob.name} Health: {new_mob.health}")
#     print(f"Attack Power: {new_mob.atk_power}")
#     print(f"Armor Class: {new_mob.armor_class}")
#     print(f"Weapon: {new_mob.weapon_name}")
#     print(f"weapon Damage: {new_mob.weapon_damage}")
#     print(f"Inventory: {new_mob.inventory}")
#     #
#     #     ## Attack and check if mob or player is stuned or dead
#     # new_toon.do_action(new_mob.name, new_mob.armor_class, new_toon.atk_power)
#     new_toon.do_action(new_mob)
#     if new_mob.health <= 0:
#         print(f"You have defeated the {new_mob.name}!")
#         new_toon.loot_mob(new_mob)
#         print(f"Inventory: {new_toon.inventory}")
#         break
#
#     # new_mob.do_action(new_toon.name, new_toon.armor_class, new_mob.atk_power)
#     new_mob.do_action(new_toon)
#     if new_toon.health <= 0:
#         print("You have been defeated!")
#         break
