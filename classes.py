## Game Classes and items
import random


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
            "rusty dagger": (1, 4, 0),
            "bronze sword": (3, 10, 1),
            "Mace of the Gods": (5, 15, 8),
            "broken wand": (1, 2, 0),
            "glowing wand": (3, 6, 3),
            "Wand of Eternal Destruction": (6, 12, 10),
        }


## CHAR CLASS FOR ALL PLAYERS AND NPCS
class Char:
    def __init__(self, name, health, atk_power, armor_class):
        self.name = name
        self.health = health
        self.atk_power = atk_power
        self.ac = armor_class
        self.inventory = {}
        self.mana = 0

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
        """
        total_roll = random.randint(1, 20) + hit_chance
        return total_roll >= ac

    def heal_self(self, heal_amount=(), spell_pwr=0):
        """
        heal_amount is a tuple that holds the min and max heal amount of any
        item, spell, or ability. A random num between min and max heal_amount
        is returned.
        """
        total_heal = (random.randint(heal_amount[0], heal_amount[1])) + spell_pwr
        return total_heal


class Warrior(Char):
    def __init__(self, name):
        super().__init__(name, health=50, atk_power=5, armor_class=16)
        self.inventory["potions"] = ()

    def test(self):
        return "Testing"


new_toon = Warrior("bob")
print(new_toon.test())
# new_toon = Warrior("bob", 100, 3, 15)
# print(new_toon.attack_dmg(3, (1, 5)))
# print(new_toon.hit_check(10, new_toon.atk_power))
