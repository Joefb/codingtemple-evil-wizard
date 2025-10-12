## Game Classes and items
import random
import os


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
        self.inventory = {}
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

    def do_action(self, mob_name, mob_ac, atk_power):
        """
        Checks if player is stunned, if so they cannot act.
        Iterates through the actions list and prints them out player. Actions list
        are function names in each class. getattr is used to call the function.
        """
        # Check if player is stunned
        # if stuned decrament stun duration and skip turn
        if self.stun_duration > 0:
            self.stun_duration -= 1
            print("You are stunned and cannot act this turn!")
            return

        # used for numbering the actions
        counter = 1

        # list out actions
        print("What will you do?")
        print("Choose a action:")
        for skill in self.actions:
            print(f"{counter}) {skill}")
            counter += 1

        # gets player action and does a hit check
        action = int(input("-> "))
        if action == 1 or action == 2 or action == 3:
            hit, is_crit = self.hit_check(mob_ac, atk_power)

            if not hit:
                print(f"You miss the {mob_name}!")
                return False

        # gets the action from action list in the child class and calls the method
        if action == 1:
            self.action = self.actions[0]
            self.action_method = getattr(self, self.action)
            self.action_method(mob_name, is_crit)

        if action == 2:
            self.action = self.actions[1]
            self.action_method = getattr(self, self.action)
            self.action_method(mob_name, is_crit)

        if action == 3:
            self.action = self.actions[2]
            self.action_method = getattr(self, self.action)
            self.action_method(mob_name, is_crit)


class Warrior(Char):
    def __init__(self, name):
        super().__init__(name, health=50, atk_power=5, armor_class=12)

        # set starting weapon and get its damage from weapons dict in Items class
        self.weapon_name = "rusty dagger"
        self.weapon_damage = self.weapons.get(self.weapon_name)

        # set the atk_power to include the weapon's atk_power bonus
        self.atk_power += self.weapon_damage[2]

        # warrior actions. Each action is a method in this class
        self.actions = ["strike", "bash", "enrage"]

        # set bash damage and cooldown
        self.bash_damage = (1, 2, 0)  # (min, max, atk_power)
        self.bash_cooldown = 0

        # enrage cooldown
        self.enrage_cooldown = 0

    def strike(self, mob_name, is_crit):
        # Rolls damage and sets attack message
        damage = self.attack_dmg(self.atk_power, self.weapon_damage)

        # enrage is +10 to atk_power, hit chance, and always crits for 3 turns
        # 10 turn cooldown
        if self.enrage_cooldown > 3:
            damage = damage + 10 * 2
            self.enrage_cooldown -= 1
        elif self.enrage_cooldown > 0:
            self.enrage_cooldown -= 1

        attack_mesge = f"You strike the {mob_name} for {damage} damage!"

        # check for crit and apply damage
        if is_crit:
            damage = damage * 2
            new_mob.health -= damage
            print("You land a CRITICAL STRIKE!")
            print(attack_mesge)
        else:
            print(attack_mesge)
            new_mob.health -= damage

    def bash(self, mob_name, is_crit):
        damage = self.attack_dmg(1, self.bash_damage)
        attack_mesge = (
            f"You bash the {mob_name} for {damage} damage!\nThe {mob_name} is stunned!"
        )
        # check if is on bash cooldown
        if self.bash_cooldown > 0:
            print(f"Bash is on cooldown for {self.bash_cooldown} more turns!")
            self.bash_cooldown -= 1
            return
        # check for crit and apply damage and stun
        elif is_crit:
            damage = damage * 2
            new_mob.health -= damage
            new_mob.stun_duration = 2
            self.bash_cooldown = 2
            print("You land a CRITICAL STRIKE!")
            print(attack_mesge)
        else:
            new_mob.stun_duration = 2
            new_mob.health -= damage
            self.bash_cooldown = 2
            print(attack_mesge)

    def enrage(self, mob_name, is_crit):
        if self.enrage_cooldown > 0:
            print(f"Enrage is on cooldown for {self.enrage_cooldown} more turns!")
        else:
            self.enrage_cooldown = 10
            self.health += 20
            print("You ENRAGE!")
            print("You heal 20 hitpoints!")
            print("For 3 turns Strike has a +10 hit chance, damage, and always crits!")


## GOBILN MOB CLASS
class Mob(Char):
    def __init__(self, name):
        super().__init__(name, health=25, atk_power=2, armor_class=10)
        self.actions = ["claws", "kicks", "spits"]
        self.inventory = {}

    def do_action(self, mob_name, mob_ac, atk_power):
        """
        Iterates through the actions list and prints them out player. Actions list
        are function names in each class. getattr is used to call the function.
        """
        if self.stun_duration > 0:
            self.stun_duration -= 1
            print(f"The {self.name} is stunned and cannot act this turn!")
            return

        random_action = random.randint(1, 3)

        if random_action == 1 or random_action == 2 or random_action == 3:
            hit, is_crit = self.hit_check(mob_ac, atk_power)

            if not hit:
                print(f"The {self.name} misses you!")
                return False

        if random_action == 1:
            self.action = self.actions[0]
            self.action_method = getattr(self, self.action)
            self.action_method(mob_name, is_crit)

        if random_action == 2:
            self.action = self.actions[1]
            self.action_method = getattr(self, self.action)
            self.action_method(mob_name, is_crit)

        if random_action == 3:
            self.action = self.actions[2]
            self.action_method = getattr(self, self.action)
            self.action_method(mob_name, is_crit)

    def claws(self, _, is_crit):
        damage = self.attack_dmg(self.atk_power, (1, 4))
        attack_mesge = f"The {self.name} snarles at you and slashes you with their claws for {damage} of damage!"
        if is_crit:
            print(f"The {self.name} lands a CRITICAL STRIKE!")
            damage = damage * 2
            new_toon.health -= damage
            print(attack_mesge)
        else:
            new_toon.health -= damage
            print(attack_mesge)

    def kicks(self, _, is_crit):
        damage = self.attack_dmg(self.atk_power, (1, 6))
        attack_mesge = f'"Smelly human die! No take my shiny!" the {self.name} screams as they kick you for {damage} damage!'
        if is_crit:
            print(f"The {self.name} lands a CRITICAL STRIKE!")
            damage = damage * 2
            new_toon.health -= damage
            print(attack_mesge)
        else:
            new_toon.health -= damage
            print(attack_mesge)

    def spits(self, _, is_crit):
        damage = self.attack_dmg(self.atk_power, (1, 1))
        attack_mesge = f"The {self.name} spits in your eyes for {damage} damage as they smile and kackle! You can't see and are stunned!"
        if is_crit:
            print(f"The {self.name} lands a CRITICAL STRIKE!")
            damage = damage * 2
            new_toon.health -= damage
            new_toon.stun_duration = 1
            print(attack_mesge)
        else:
            new_toon.health -= damage
            new_toon.stun_duration = 1
            print(attack_mesge)


new_toon = Warrior("bob")
new_mob = Mob("goblin")


#### TESTING AREA CODE #######

print(f"You encounter a {new_mob.name}!")
##input("Press enter to continue...")
print("")

while new_toon.health > 0 and new_mob.health > 0:
    print("--------- Toon Status ---------")
    print(f"{new_toon.name} Health: {new_toon.health}")
    print(f"{new_mob.name} Health: {new_mob.health}")
    print(f"Attack Power: {new_toon.atk_power}")
    print(f"Armor Class: {new_toon.armor_class}")
    print(f"Weapon: {new_toon.weapon_name}")
    print(f"weapon Damage: {new_toon.weapon_damage}")
    print("---------------------------")
    print("")
    print("--------- Mob Status ---------")
    print(f"{new_mob.name} Health: {new_mob.health}")
    print(f"Attack Power: {new_mob.atk_power}")
    print(f"Armor Class: {new_mob.armor_class}")
    print(f"Weapon: {new_mob.weapon_name}")
    print(f"weapon Damage: {new_mob.weapon_damage}")

    ## Attack and check if mob or player is stuned or dead
    new_toon.do_action(new_mob.name, new_mob.armor_class, new_toon.atk_power)
    if new_mob.health <= 0:
        print(f"You have defeated the {new_mob.name}!")
        break
    # elif new_toon.stun_duration > 0:
    #     print("You are stunned and cannot act this turn!")
    #     new_toon.stun_duration -= 1
    # else:
    # print("What will you do?!")
    # new_toon.do_action(new_mob.name, new_mob.armor_class, new_toon.atk_power)

    new_mob.do_action(new_toon.name, new_toon.armor_class, new_mob.atk_power)
    if new_toon.health <= 0:
        print("You have been defeated!")
        break
    # elif new_mob.stun_duration > 0:
    #     print(f"The {new_mob.name} is stunned and cannot act this turn!")
    #     new_mob.stun_duration -= 1
    # else:
    #     new_mob.do_action(new_toon.name, new_toon.armor_class, new_mob.atk_power)


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
