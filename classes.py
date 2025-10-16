## Game Classes and items
import random
import re


## ITEMS
class Items:
    def __init__(self):
        self.items = {
            "lesser heal potion": (5, 15),
            "greater heal potion": (20, 50),
            "lesser mana potion": (5, 15),
            "greater mana potion": (20, 50),
        }

        self.weapons = {
            "fists": (1, 2, 0),
            "rusty dagger": (1, 4, 0),
            "bronze sword": (3, 10, 1),
            "Mace of the Ancient Gods": (5, 15, 8),
            "broken wand": (1, 2, 0),
            "glowing wand": (3, 6, 3),
            "Wand of Eternal Destruction": (6, 12, 10),
        }


## CHAR CLASS FOR ALL PLAYERS AND NPCS
class Char(Items):
    def __init__(self, name, health, atk_power, armor_class):
        super().__init__()
        self.name = name
        self.health = health
        self.atk_power = atk_power
        self.armor_class = armor_class
        self.mana = 0
        self.actions = []
        # inventory
        self.inventory = []
        self.item_key = ""
        self.weapon_name = "Fists"
        self.weapon_damage = (1, 2)
        self.stun_duration = 0

    def attack_dmg(self, atk_power, wep_dmg=()):
        """
        Returns the attack damage. wep_dmg is a tuple holding the min and max
        damage of the weapon. A random number is rolled between the min and max
        damage of the weapon + the atk_power. The total is returned.
        """
        return (random.randint(wep_dmg[0], wep_dmg[1])) + atk_power

    def hit_check(self, ac, hit_chance):
        """
        This method takes in the armor class of the target and the hit chance of the attacker.
        A random 20 + the hit chance is rolled, if the number is
        above the targets ac the attack hits, if not it fails. Returns a bools.
        If the roll is a natural 20, it is a critical hit and the second return

        """
        roll = random.randint(1, 20)
        total_roll = roll + hit_chance
        if roll == 20:
            return roll >= ac, True
        return total_roll >= ac, False

    def heal_self(self, heal_amount=(), spell_pwr=0):
        """
        heal_amount is a tuple that holds the min and max heal amount of any
        item, spell, or ability. A random num between min and max heal_amount
        is returned.
        """
        total_heal = (random.randint(heal_amount[0], heal_amount[1])) + spell_pwr
        return total_heal

    def drink_potion(self):
        """
        Handles drinking potions from the players inventory.
        Iterates through the inventory and lists only potions.
        Uses the potion, and removes potion from inventory
        Input validation is done.
        """
        potion_idx = []
        print("----- Potions Inventory -----")
        print("Choose a potion to drink:")
        for idx, item in enumerate(self.inventory):
            if item in self.items:
                potion_idx.append(idx)
                print(f"{idx}: {item}")
                print("-----------------------------")
        try:
            input_idx = int(input("-> "))
            if input_idx not in potion_idx:
                print("Invalid input. Please enter a valid potion number.")
                self.drink_potion()

            elif input_idx in potion_idx:
                potion_name = self.inventory[input_idx]

                if "heal" in potion_name:
                    heal_amount = self.items.get(potion_name)
                    healed = self.heal_self(heal_amount)
                    self.health += healed
                    print(
                        f"You drink the {potion_name} and heal for {healed} hitpoints!"
                    )
                    self.inventory.remove(potion_name)

                elif "mana" in potion_name:
                    mana_amount = self.items.get(potion_name)
                    manad = self.heal_self(mana_amount)
                    self.mana += manad
                    print(f"You drink the {potion_name} and restore {manad} mana!")
                    self.inventory.remove(potion_name)

        except ValueError:
            print("Invalid number. Please enter a valid potion number.")
            self.drink_potion()

    def loot_mob(self, mob):
        if len(mob.inventory) > 0:
            for item in mob.inventory:
                self.inventory.append(item)
                return f"You loot a {item} from the {mob.name}!"

    def equip_weapon(self):
        """
        Handles equipping weapons from the players inventory.
        Iterates through the inventory and lists only weapons.
        Input validation is done.
        Prints weapon stats when equipped.
        """
        weapon_idx = []
        print("----- Weapons Inventory -----")
        print("Choose a weapon to equip:")
        for idx, item in enumerate(self.inventory):
            if item in self.weapons:
                weapon_idx.append(idx)
                print(f"{idx}: {item}")
                print("-----------------------------")

        try:
            equip_idx = int(input("-> "))
            if equip_idx not in weapon_idx:
                print("Invalid input. Please enter a valid weapon number.")
                self.equip_weapon()

            elif equip_idx in weapon_idx:
                item = self.inventory[equip_idx]
                print(f"You equip the {item}!")
                self.weapon_name = item
                self.weapon_damage = self.weapons.get(item)
                print("Weapon Stats:")
                print(f"Damage: {self.weapon_damage[0]} - {self.weapon_damage[1]}")
                print(f"Attack Power Bonus: {self.weapon_damage[2]}")
                print(f"Hit Chance Bonus: {self.weapon_damage[2]}")

        except ValueError:
            print("Invalid number. Please enter a valid weapon number.")
            self.equip_weapon()

    # def do_action(self, mob, mob_ac, atk_power):
    def do_action(self, action, mob):
        """
        Iterates through the actions list and prints them out player. Actions list
        are function names in each class. getattr is used to call the function.
        stun check is done,
        """
        # Check if player is stunned
        # if stuned decrament stun duration and skip turn
        if self.stun_duration > 0:
            self.stun_duration -= 1
            return "You are stunned and cannot act this turn!"

        # used for numbering the actions
        # counter = 1
        # # list out actions
        # # preform input validation
        # while True:
        #     try:
        #         print("What will you do?")
        #         print("Choose a action:")
        #         for skill in self.actions:
        #             print(f"{counter}) {skill}")
        #             counter += 1
        #
        #         # gets player action
        #         action = int(input("-> "))
        #         if action < 1 or action > len(self.actions):
        #             counter = 1
        #             print("Invalid input. Please enter a action number.")
        #             continue
        #
        #     except ValueError:
        #         counter = 1
        #         print("Invalid input. Please enter a action number.")
        #
        #     else:
        #         break

        # preform hit check
        if action == 1 or action == 2 or action == 3:
            hit, is_crit = self.hit_check(mob.armor_class, self.atk_power)

            if not hit:
                return f"You miss the {mob.name}!"

        # gets the action from action list in the child class and calls the method
        # in the instance method
        if action == 1:
            self.action = self.actions[0]
            self.action_method = getattr(self, self.action)
            return self.action_method(mob, is_crit)

        if action == 2:
            self.action = self.actions[1]
            self.action_method = getattr(self, self.action)
            self.action_method(mob, is_crit)

        if action == 3:
            self.action = self.actions[2]
            self.action_method = getattr(self, self.action)
            self.action_method(mob, is_crit)

        # drink potion
        if action == 4:
            # cheks if there are any potions in inventory
            count_items = []
            for idx, item in enumerate(self.inventory):
                if item in self.items:
                    count_items.append(idx)
            if len(count_items) == 0:
                return "You have no potions in your inventory!"

            self.action = self.actions[3]
            self.action_method = getattr(self, self.action)
            self.action_method()

        # equip weapon
        if action == 5:
            # checks if there are any weapons in inventory
            count_weapons = []
            for idx, wep in enumerate(self.inventory):
                if wep in self.weapons:
                    count_weapons.append(idx)
            if len(count_weapons) == 0:
                return "You have no weapons in your inventory!"

            self.action = self.actions[4]
            self.action_method = getattr(self, self.action)
            self.action_method()


class Warrior(Char):
    def __init__(self, name):
        super().__init__(name, health=50, atk_power=5, armor_class=12)

        # set starting weapon and get its damage from weapons dict in Items class
        self.weapon_name = "fists"
        self.weapon_damage = self.weapons.get(self.weapon_name)
        # set the atk_power to include the weapon's atk_power bonus
        self.atk_power += self.weapon_damage[2]
        # warrior actions. Each action is a method in this class
        self.actions = ["strike", "bash", "enrage", "drink_potion", "equip_weapon"]
        # set bash damage and cooldown
        self.bash_damage = (1, 2, 0)  # (min, max, atk_power)
        self.bash_cooldown = 0
        # enrage cooldown
        self.enrage_cooldown = 0
        # inventory
        self.inventory = ["fists"]

    def strike(self, mob, is_crit):
        # Rolls damage and sets attack message
        damage = self.attack_dmg(self.atk_power, self.weapon_damage)

        # Check if enrage is active and apply bonus damage and decrament duration
        if self.enrage_cooldown > 7:
            damage = damage + 10 * 2
            self.enrage_cooldown -= 1

        # elif self.enrage_cooldown == 7:
        #     print("You are no longer Enraged!")
        #     self.enrage_cooldown -= 1

        elif self.enrage_cooldown > 0:
            self.enrage_cooldown -= 1

        # check for crit and apply damage
        if is_crit:
            damage += damage * 2
            mob.health -= damage
            if self.enrage_cooldown == 7:
                return f"""
                            You are no longer Enraged!
                            CRITICAL STRIKE! You strike the {mob.name} for {damage} damage!
                       """
        elif is_crit and self.enrage_cooldown < 7:
            mob.health -= damage
            return f"CRITICAL STRIKE! You strike the {mob.name} for {damage} damage!"

        if self.enrage_cooldown == 7:
            mob.health -= damage
            return f"You are no longer Enraged!\nYou strike the {mob.name} for {damage} damage!"

        mob.health -= damage
        return f"You strike the {mob.name} for {damage} damage!"

    def bash(self, mob, is_crit):
        damage = self.attack_dmg(1, self.bash_damage)
        # check if is on bash cooldown
        if self.bash_cooldown > 0:
            self.bash_cooldown -= 1
            return f"Bash is on cooldown for {self.bash_cooldown} more turns!"

        # check for crit and apply damage and stun
        elif is_crit:
            damage = damage * 2
            mob.health -= damage
            mob.stun_duration = 2
            self.bash_cooldown = 2
            return f"You land a CRITICAL STRIKE! You bash the {mob.name} for {damage} damage!\nThe {mob.name} is stunned!"
        else:
            mob.stun_duration = 2
            mob.health -= damage
            self.bash_cooldown = 2
            return f"You bash the {mob.name} for {damage} damage!\nThe {mob.name} is stunned!"

    # enrage is +10 to atk_power, hit chance, and always crits for 3 turns
    # 10 turn cooldown
    def enrage(self, _mob, _is_crit):
        if self.enrage_cooldown > 0:
            self.enrage_cooldown -= 1
            return f"Enrage is on cooldown for {self.enrage_cooldown} more turns!"
        else:
            self.enrage_cooldown = 10
            self.health += 20
            return """
                    You ENRAGE!
                    You heal for 20 hitpoints!
                    For 3 turns Strike has a +10 hit chance, damage, and always crits!
                    """


## GOBILN MOB CLASS
class Mob(Char):
    def __init__(self, name):
        super().__init__(name, health=25, atk_power=2, armor_class=10)
        self.actions = ["claws", "kicks", "spits"]
        self.inventory = ["lesser heal potion"]

    def do_action(self, _action, mob):
        """
        actions list are function names in each class.
        getattr is used to call the function.
        """
        if self.stun_duration > 0:
            self.stun_duration -= 1
            return f"The {self.name} is stunned and cannot act this turn!"

        random_action = random.randint(1, 3)

        if random_action == 1 or random_action == 2 or random_action == 3:
            hit, is_crit = self.hit_check(mob.armor_class, self.atk_power)

            if not hit:
                return f"The {self.name} misses you!"

        if random_action == 1:
            self.action = self.actions[0]
            self.action_method = getattr(self, self.action)
            self.action_method(mob, is_crit)

        if random_action == 2:
            self.action = self.actions[1]
            self.action_method = getattr(self, self.action)
            self.action_method(mob, is_crit)

        if random_action == 3:
            self.action = self.actions[2]
            self.action_method = getattr(self, self.action)
            self.action_method(mob, is_crit)

    def claws(self, mob, is_crit):
        damage = self.attack_dmg(self.atk_power, (1, 4))
        if is_crit:
            damage = damage * 2
            mob.health -= damage
            return f"""
                    The {self.name} lands a CRITICAL STRIKE!
                    The {self.name} snarles at you and slashes you with their claws for {damage} of damage!
                   """
        else:
            mob.health -= damage
            return f"The {self.name} snarles at you and slashes you with their claws for {damage} of damage!"

    def kicks(self, mob, is_crit):
        damage = self.attack_dmg(self.atk_power, (1, 6))

        if is_crit:
            damage = damage * 2
            mob.health -= damage
            return f"""
                    The {self.name} lands a CRITICAL STRIKE!
                    "Smelly human die! No take my shiny!" the {self.name} screams as they kick you for {damage} damage!
                    """
        else:
            mob.health -= damage
            return f'"Smelly human die! No take my shiny!" the {self.name} screams as they kick you for {damage} damage!'

    def spits(self, mob, is_crit):
        damage = self.attack_dmg(self.atk_power, (1, 1))
        if is_crit:
            damage = damage * 2
            mob.health -= damage
            mob.stun_duration = 1
            return f"""
                    The {self.name} lands a CRITICAL STRIKE!
                    The {self.name} spits in your eyes for {damage} damage as they smile and kackle! You can't see and are stunned!
                    """
        else:
            mob.health -= damage
            mob.stun_duration = 1
            return f"The {self.name} spits in your eyes for {damage} damage as they smile and kackle! You can't see and are stunned!"


#### TESTING AREA CODE #######
# new_toon = Warrior("bob")
# new_mob = Mob("goblin")
#
# print(f"You encounter a {new_mob.name}!")
# # input("Press enter to continue...")
# print("")
#
# while new_toon.health > 0 and new_mob.health > 0:
#     print("--------- Toon Status ---------")
#     print(f"{new_toon.name} Health: {new_toon.health}")
#     print(f"{new_mob.name} Health: {new_mob.health}")
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
#
#     ## Attack and check if mob or player is stuned or dead
#     # new_toon.do_action(new_mob.name, new_mob.armor_class, new_toon.atk_power)
#     new_toon.do_action(new_mob)
#     if new_mob.health <= 0:
#         print(f"You have defeated the {new_mob.name}!")
#         new_toon.loot_mob(new_mob)
#         print(f"Inventory: {new_toon.inventory}")
#         break
#
#     # elif new_toon.stun_duration > 0:
#     #     print("You are stunned and cannot act this turn!")
#     #     new_toon.stun_duration -= 1
#     # else:
#     # print("What will you do?!")
#     # new_toon.do_action(new_mob.name, new_mob.armor_class, new_toon.atk_power)
#     #
#
#     # new_mob.do_action(new_toon.name, new_toon.armor_class, new_mob.atk_power)
#     new_mob.do_action(new_toon)
#     if new_toon.health <= 0:
#         print("You have been defeated!")
#         break


# elif new_mob.stun_duration > 0:
#     print(f"The {new_mob.name} is stunned and cannot act this turn!")
#     new_mob.stun_duration -= 1
# else:
#     new_mob.do_action(new_toon.name, new_toon.armor_class, new_mob.atk_power)


# EQUIP WEAPON EXAMPLE
# if item in self.weapons:
#     print(f"You equip the {item}!")
#     self.weapon_name = item
#     self.weapon_damage = self.weapons.get(item)


# new_toon.do_action(new_mob.name, new_mob.armor_class, new_toon.atk_power)
# print(
#     f"new_toon: {new_toon.name}, {new_toon.health}, {new_toon.atk_power}, {new_toon.armor_class}"
# )
# print(f"{new_toon.weapon_damage}")
# print(type(new_toon.weapon_damage))
# print(new_mob.armor_class)
# print(new_toon.armor_class)
## INVENTORY EXAMPLES
# new_toon.item_key = "lesser heal potion"
# print(f"{new_toon.name} has found a {new_toon.items.get(new_toon.item_key)}")
# new_toon.inventory[new_toon.item_key] = new_toon.items.get(new_toon.item_key)
# print(f"inventory {new_toon.inventory}")
# new_toon.do_action()


# new_toon.inventory(new_toon.items.get("lesser heal potion"))
# print(f"{new_toon.name} has found a {new_toon.items.get(item_key)}")
# new_toon.inventory["lesser heal potion"] = new_toon.items.get("lesser heal potion")
# print(f"item: {new_toon.items}")

# print(new_toon.test())
# new_toon = Warrior("bob", 100, 3, 15)
# print(new_toon.attack_dmg(3, (1, 5)))
# print(new_toon.hit_check(10, new_toon.atk_power))
#
# def do_action(self, mob_name, mob_ac, atk_power):
#     counter = 1
#
#     print("Choose a action:")
#     for skill in self.actions:
#         print(f"{counter}) {skill}")
#         counter += 1
#
#     action = int(input("-> "))
#     if action == 1 or action == 2:
#         hit, is_crit = self.hit_check(mob_ac, atk_power)
#
#         if not hit:
#             # return f"You miss the {mob_name}!"
#             print(f"You miss the {mob_name}!")
#             return False
#
#     if action == 1:
#         self.strike(mob_name, is_crit)
#
#     if action == 2:
#         pass
#
#     if action == 3:
#         pass
