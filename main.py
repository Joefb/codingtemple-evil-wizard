import random
import os
import classes


class Game:
    def __init__(self, player):
        self.player = player
        # self.mob = mob

    def display_status(self, player, mob):
        """Displays a status 'bar' for player and mob."""
        status = f"""
{"=" * 40}
| Player: {player.name:<10} 
{"-" * 40}
| Class:{player.__class__.__name__} | HP: {player.health:>3} | ATK: {player.atk_power:>2} | AC: {player.armor_class:>} 
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


def main():
    print("Welcome to Evil Wizard!!")
    input("Press enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")
    print("Create your character:")
    print("Enter your name young adventurer: ")
    name = input("-> ")
    print("")
    print("Choose your class:")
    print("1) Warrior")
    print("2) Druid")

    while True:
        try:
            class_choice = int(input("-> "))
            if class_choice < 1 or class_choice > 2:
                print("Invalid input. Please enter a valid action number.")
                continue

            if class_choice == 1:
                new_toon = classes.Warrior(name)
                break
            elif class_choice == 2:
                new_toon = classes.Druid(name)
                break

        except ValueError:
            print("Invalid input. Please enter a valid action number.")
            continue

    game = Game(new_toon)
    # new_mob = classes.Goblin("Goblin", 30, 3, 11, [])
    new_mob = classes.Goblin(
        "Scrawny Goblin", 15, 3, 8, ["rusty dagger", "lesser heal potion"]
    )
    game.battle(new_toon, new_mob)


if __name__ == "__main__":
    main()

#### TESTING AREA CODE #######
