import random
import os
import classes


class Game:
    def __init__(self, player, mob):
        self.player = player
        self.mob = mob

    def display_status(self, player, mob):
        """Displays a status 'bar' for player and mob."""
        status = f"""
{"=" * 40}
| Player: {player.name:<10} 
{"-" * 40}
| HP: {player.health:>3} | ATK: {player.atk_power:>2} | AC: {player.armor_class:>} 
{"-" * 40}
| Weapon: {player.weapon_name:<20} 
| Inventory: {", ".join(player.inventory) if player.inventory else "Empty":<30} 
{"=" * 40}
            """
        return status

    def battle(self, player, mob):
        """
        Handles battle loop with a clean UI: status bar, damage results, and actions.
        """
        # Clear the console
        os.system("cls" if os.name == "nt" else "clear")
        print(f"You encounter a {mob.name}!")
        input("Press enter to continue...")
        print("")

        while player.health > 0 and mob.health > 0:
            # Clear console
            os.system("cls" if os.name == "nt" else "clear")

            # Display status bar
            print(self.display_status(player, mob))

            # Display damage results
            if "player_action_result" in locals() and "mob_action_result" in locals():
                print("=== Battle Results ===")
                print(player_action_result)
                print(mob_action_result)
                print("=" * 20)

            # Display player actions
            print(f"\nMob: {mob.name:}")
            print("=== Actions ===")
            for idx, skill in enumerate(player.actions, 1):
                print(f"{idx}) {skill}")
            print("=" * 20)

            # Get player action with input validation
            try:
                action = int(input("-> "))
                if action < 1 or action > len(player.actions):
                    print("Invalid input. Please enter a valid action number.")
                    # input("Press enter to continue...")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid action number.")
                input("Press enter to continue...")
                continue

            # Perform actions
            player_action_result = str(player.do_action(action, mob))
            if mob.health <= 0:
                print("=== Battle Results ===")
                print(player_action_result)
                print("=" * 20)
                print(self.display_status(player, mob))  # Show final status
                print(f"You have defeated the {mob.name}!")
                loot_result = player.loot_mob(mob)
                if loot_result:
                    print(loot_result)
                print(
                    f"Inventory: {', '.join(player.inventory) if player.inventory else 'Empty'}"
                )
                return

            mob_action_result = str(mob.do_action(None, player))
            if player.health <= 0:
                print(self.display_status(player, mob))  # Show final status
                print("You have been defeated!")
                return

    def print_welcome(self):
        print("Welcome to Evil Wizard!!")

    def create_char(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Create your character:")
        print("Enter your name young adventurer: ")
        name = input("-> ")
        print("")
        print("Choose your class:")
        print("1) Warrior")
        print("2) Druid")
        class_choice = input("-> ")

        if class_choice == "1":
            new_toon = classes.Warrior(name)
        elif class_choice == "2":
            new_toon = classes.Druid(name)


def main():
    new_toon = classes.Warrior("Bob")
    new_toon = classes.Druid("Bob")
    # new_mob = classes.Goblin("Goblin", 30, 3, 11)
    # new_mob = classes.Goblin("Scrawny Goblin", 15, 3, 8)
    new_mob = classes.Siren("Siren", 30, 5, 12)
    # new_mob = classes.Wizard("The Evil Wizard", 50, 5, 13)
    game = Game(new_toon, new_mob)
    game.battle(new_toon, new_mob)
    input("Press enter to continue...")


if __name__ == "__main__":
    main()

#### TESTING AREA CODE #######
# new_toon = classes.Warrior("Bob")
# new_mob = classes.Goblin("Goblin", 30, 3, 11)
# new_mob = classes.Goblin("Scrawny Goblin", 15, 3, 8)
# new_mob = classes.Siren("Siren", 30, 5, 12)
# new_mob = classes.Wizard("The Evil Wizard", 50, 5, 13)
# game = Game(new_toon, new_mob)
# game.battle(new_toon, new_mob)
# input("Press enter to continue...")
# new_mob = classes.Wizard("The Evil Wizard", 50, 5, 13)
# new_mob = classes.Goblin("Goblin", 30, 3, 11)
# new_mob = classes.Siren("Enraged Siren", 30, 5, 12)
# game.battle(new_toon, new_mob)
# new_toon = classes.Warrior("bob")
# new_mob = classes.Mob("goblin")
# game = Game(new_toon, new_mob)
# game.battle(new_toon, new_mob)
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
