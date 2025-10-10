## Game Classes
import random


class Char:
    def __init__(self, name, health, mana, atk_power, armor_class):
        self.name = name
        self.health = health
        self.mana = mana
        self.atk_power = atk_power
        self.ac = armor_class

    def attack_dmg(self, atk_power, wep_dmg=()):
        """
        Returns the attack damage. wep_dmg is a tuple holding the min and max
        damage of the weapon. A random number is rolled between the min and max
        damage of the weapon + the atk_power. The total is returned.
        """
        return random.randint(wep_dmg[0], wep_dmg[1]) + atk_power

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
        total_heal = random.randint(heal_amount[0], heal_amount[1]) + spell_pwr
        return total_heal


new_toon = Char("bob", 100, 100, 3, 15)
print(new_toon.hit_check(10, new_toon.atk_power))
