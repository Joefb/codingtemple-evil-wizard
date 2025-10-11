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
        above the targets ac the attack hits, if not it fails. Returns a bool.
        If the roll is a natural 20, it is a critical hit and the second return

        """
        roll = random.randint(1, 20)
        total_roll = roll + hit_chance

        if roll == 20:
            print("CRITICAL STRIKE!")
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
        Iterates through the actions list and prints them out player. Actions list
        are function names in each class. getattr is used to call the function.
        """
        counter = 1

        print("Choose a action:")
        for skill in self.actions:
            print(f"{counter}) {skill}")
            counter += 1

        action = int(input("-> "))
        if action == 1 or action == 2 or action == 3:
            hit, is_crit = self.hit_check(mob_ac, atk_power)

            if not hit:
                print(f"You miss the {mob_name}!")
                return False

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
        self.weapon_name = "rusty dagger"
        self.weapon_damage = self.weapons.get(self.weapon_name)
        self.atk_power += self.weapon_damage[2]
        self.actions = ["strike", "bash", "drink potion"]
        self.bash_damage = (1, 2, 0)  # (min, max, atk_power)

    def strike(self, mob_name, is_crit):
        if is_crit:
            damage = (self.attack_dmg(self.atk_power, self.weapon_damage)) * 2
            new_mob.health -= damage
            print(f"You strike the {mob_name} for {damage} damage!")
        else:
            damage = self.attack_dmg(self.atk_power, self.weapon_damage)
            print(f"You strike the {mob_name} for {damage} damage!")
            new_mob.health -= damage

    def bash(self, mob_name, is_crit):
        if is_crit:
            # damage = (self.attack_dmg(self.atk_power, self.weapon_damage)) * 2
            damage = (self.attack_dmg(1, self.bash_damage)) * 2
            new_mob.health -= damage
            new_mob.stun_duration = 2
            print(f"You bash the {mob_name} for {damage} damage!")
            print(f"The {new_mob.name} is stunned!")
        else:
            damage = self.attack_dmg(1, self.bash_damage)
            # damage = self.attack_dmg(self.atk_power, self.weapon_damage)
            # damage = self.attack_dmg(1, 2)
            print(f"You bash the {mob_name} for {damage} damage!")
            print(f"The {mob_name} is stunned!")
            new_mob.stun_duration = 2
            new_mob.health -= damage

    def drink_potion(self, mob_name, is_crit):
        pass


## GOBILN MOB CLASS
class Mob(Char):
    def __init__(self, name):
        super().__init__(name, health=25, atk_power=2, armor_class=10)
        self.actions = ["claws", "kicks", "spits"]

    def claws(self, _, is_crit):
        if is_crit:
            damage = (self.attack_dmg(self.atk_power, (1, 4))) * 2
            new_toon.health -= damage
            print(f"The {self.name} claws you for {damage} damage!")
        else:
            damage = self.attack_dmg(self.atk_power, (1, 4))
            new_toon.health -= damage
            print(f"The {self.name} claws you for {damage} damage!")

    def kicks(self, _, is_crit):
        if is_crit:
            damage = (self.attack_dmg(self.atk_power, (1, 6))) * 2
            new_toon.health -= damage
            print(f"The {self.name} kicks you for {damage} damage!")
        else:
            damage = self.attack_dmg(self.atk_power, (1, 6))
            new_toon.health -= damage
            print(f"The {self.name} kicks you for {damage} damage!")

    def spits(self, _, is_crit):
        if is_crit:
            damage = (self.attack_dmg(self.atk_power, (1, 1))) * 2
            new_toon.health -= damage
            new_toon.stun_duration = 1
            print(
                f"The {self.name} spits in your eyes {damage} damage and you are stuned!!"
            )
        else:
            damage = self.attack_dmg(self.atk_power, (1, 1))
            new_toon.health -= damage
            new_toon.stun_duration = 1
            print(
                f"The {self.name} spits in your eyes for {damage} damage and you are stuned!!"
            )


new_toon = Warrior("bob")
new_mob = Mob("goblin")


#### TESTING AREA #######

print(f"You encounter a {new_mob.name}!")
##input("Press enter to continue...")
print("")

while new_toon.health > 0 and new_mob.health > 0:
    print("--------- Status ---------)")
    print(f"{new_toon.name} Health: {new_toon.health}")
    print(f"{new_mob.name} Health: {new_mob.health}")
    print("---------------------------")

    ## Attack and check if mob or player is stuned or dead
    if new_mob.health <= 0:
        print(f"You have defeated the {new_mob.name}!")
    elif new_toon.stun_duration > 0:
        print("You are stunned and cannot act this turn!")
        new_toon.stun_duration -= 1
    else:
        print("What will you do?!")
        new_toon.do_action(new_mob.name, new_mob.armor_class, new_toon.atk_power)

    if new_toon.health <= 0:
        print("You have been defeated!")
    elif new_mob.stun_duration > 0:
        print(f"The {new_mob.name} is stunned and cannot act this turn!")
        new_mob.stun_duration -= 1
    else:
        new_mob.do_action(new_toon.name, new_toon.armor_class, new_mob.atk_power)


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
