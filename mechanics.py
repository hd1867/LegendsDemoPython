"""
RP Mechanics
To do:Movement/World, Savegames, Procedural Generation, NPCs, Dialgoue Options, Vivid Descriptions
"""

import random
import time
from dataclasses import dataclass


@dataclass
class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


@dataclass
class weapon:
    """
    To Do: Durability
    """

    def __init__(self, name, typ, damage_die, damage_type, mod, weight):
        self.name = name  # str
        self.typ = typ  # str
        self.damage_die = damage_die  # int
        self.damage_type = damage_type  # str
        self.mod = mod  # int
        self.weight = weight  # int

    def inspect(self):
        print("\n" + self.name + ":\n" + "Weapon Type: " + self.typ
              + "\n" + "Damage Type: " + self.damage_type + "\n" + "Weight: " + str(self.weight))

    def attack(self, target, attacker):
        damage = roll(self.damage_die) + self.mod
        if isinstance(attacker, player):
            damage += attacker.wep_exp[attacker.equipped_wep.typ] // 100
            attacker.wep_exp[attacker.equipped_wep.typ] += roll(
                attacker.equipped_wep.damage_die)
            target.health -= damage

        else:
            target.current_health -= damage

        print(self.name + " does " + str(damage)
              + " " + self.damage_type + " damage!")

    def parry(self, target, attacker):
        p_val = roll(target.equipped_wep.damage_die) + self.mod
        damage = roll(self.damage_die) + self.mod
        if isinstance(target, player):
            if p_val >= damage:
                print(target.name + " successfully parries, and counters for "
                      + str(p_val - damage) + " " + (self.damage_type) + " damage!")
                attacker.health -= (p_val - damage)
                target.wep_exp[target.equipped_wep.typ] += roll(
                    attacker.equipped_wep.damage_die)
            else:
                print(target.name + " misjudged the timing for the parry and " + attacker.name +
                      " was able to do an additional " + str(p_val + damage) + " damage!")
                target.current_health -= (p_val + damage)
        else:
            if p_val >= damage:
                print(target.name + " successfully parries, and counters for "
                      + str(p_val - damage) + " " + (self.damage_type) + " damage!")
                attacker.current_health -= (p_val - damage)
            else:
                print(target.name + " misjudged the timing for the parry and " + attacker.name +
                      " was able to do an additional " + str(p_val + damage) + " damage!")
                target.health -= (p_val + damage)
                attacker.wep_exp[attacker.equipped_wep.typ] += roll(
                    attacker.equipped_wep.damage_die)


@dataclass
class armor:

    def __init__(self, name, AC, durability, weight):
        self.name = name
        self.AC = AC
        self.durability = durability
        self.current_durability = durability
        self.weight = weight

    def inspect(self):
        print("\n" + self.name + ":\n" + "Armor Class: " + str(self.AC) + "\n" + "Current Durability: "
              + str(self.current_durability) + "\n" + "Total Durability: " + str(self.durability) + "\n" + "Weight: " + str(self.weight))


@dataclass
class player:
    """
    To Do:status effects, abilities, body parts, hunger/thirst, equipping/unequipping
    """

    def __init__(self, name, health, inventory, display_inventory, equipped_wep, equipped_armor, exp, level, agility, current_location):
        self.name = name
        self.health = health
        self.current_health = health
        self.inventory = inventory
        self.display_inventory = display_inventory
        self.equipped_wep = equipped_wep
        self.equipped_armor = equipped_armor
        self.exp = exp
        self.level = level
        self.wep_exp = {"Spear": 0, "Sword": 0,
                        "Axe": 0, "Martial": 0, "Hammer": 0}
        self.levels = [100, 300, 500, 1000, 2000, 3000, 4000, 5000,
                       8000, 11000, 15000, 20000, 25000, 30000, 40000, 50000, 100000]
        self.agility = agility
        self.stance = None
        self.status = None
        self.current_location = current_location

    def inspect(self):
        print("\n" + self.name + ":\n" + "Health: " + str(self.current_health) + "/" + str(self.health) + "\n" + "Inventory: " + str(self.display_inventory) + "\n" + "Equipped Weapon: "
              + self.equipped_wep.name + "\n" + "Equipped Armor: " + self.equipped_armor.name + "\n" + "Level " + str(self.level) + "\n" + "Weapon Experience" + str(self.wep_exp))

    def get_xp(self, amount):
        self.exp += amount
        if self.exp >= self.levels[self.level - 1]:
            print("Level Up!")
            self.level += 1
            self.health += random.randrange(5, 13)
            self.agility += random.randrange(0, 3)
            self.get_xp(0)
        else:
            return

    def equip(self, item):
        if item.name in self.display_inventory:
            if isinstance(item, weapon):
                self.inventory += [self.equipped_wep]
                self.display_inventory += [self.equipped_wep.name]
                self.equipped_wep = item
                self.inventory.remove(item)
                self.display_inventory.remove(item.name)
                print(item.name + " was equipped!")
            elif isinstance(item, armor):
                self.inventory += [self.equipped_armor]
                self.display_inventory += [self.equipped_armor.name]
                self.equipped_armor = item
                self.inventory.remove(item)
                self.display_inventory.remove(item.name)
            else:
                print("This item is not equippable!")
        else:
            print("You don't have this item!")

    def change_stance(self, stance):
        stance = stance.lower()
        if self.equipped_wep.typ != "Martial":
            print("You cannot change stances while wielding a non-martial weapon!")
            return
        elif stance == "brawler" and self.wep_exp["Martial"] >= 100:
            print(
                "You ball your hands into fists, preparing to put all of your strength into each blow")
            self.equipped_wep.name = "Fist"
            self.equipped_wep.damage_die = 4
            self.equipped_wep.mod = 1
            self.equipped_wep.weight = 1
        elif stance == "kicker" and self.wep_exp["Martial"] >= 200:
            print(
                "You bend your knees and curl your toes, ready to unleash devastating kicks")
            self.equipped_wep.name = "Leg"
            self.equipped_wep.damage_die = 6
            self.equipped_wep.mod = 1
            self.equipped_wep.weight = 0
        elif stance == "arts" and self.wep_exp["Martial"] >= 500:
            print("You take a proper martial arts stance, your punches and kicks having advanced to a point past amateurism")
            self.equipped_wep.name = "Hands and Feet"
            self.equipped_wep.damage_die = 8
            self.equipped_wep.mod = 3
            self.equipped_wep.weight = -2

    def move(self, direction):
        if direction == "north":
            self.current_location.x -= 1
        if direction == "south":
            self.current_location.x += 1
        if direction == "west":
            self.current_location.y -= 1
        if direction == "east":
            self.current_location.y += 1
        if direction == "northwest":
            self.current_location.x -= 1
            self.current_location.y -= 1
        if direction == "southwest":
            self.current_location.x += 1
            self.current_location.y -= 1
        if direction == "northeast":
            self.current_location.x -= 1
            self.current_location.y += 1
        if direction == "southeast":
            self.current_location.x += 1
            self.current_location.y += 1


@dataclass
class environment:
    """
    Used to keep track of and display the map
    """

    def __init__(self, name, width, height, present, passive, doors, items):
        self.name = name
        self.width = width
        self.height = height
        self.present = present
        self.passive = passive
        self.doors = doors  # list of points
        self.items = items

    def chart(self):
        dot = point(0, 0)
        for w in range(self.height):
            for h in range(self.width):
                dot = point(w, h)
                if any(creature.current_location.x == dot.x and creature.current_location.y == dot.y for creature in self.present):
                    for creature in self.present:
                        if creature.current_location.x == dot.x and creature.current_location.y == dot.y:
                            print(" " + creature.name[0] + " ", end="")

                elif any(door.location.x == dot.x and door.location.y == dot.y for door in self.doors):
                    for door in self.doors:
                        if door.location.x == dot.x and door.location.y == dot.y:
                            print(" " + str(chr(254)) + " ", end="")

                else:
                    print(" . ", end="")

            print("\n")
        print("\n")

    def recieve(self, creature, fro, door):
        self.present += [creature]
        creature.current_location = door.location
        fro.present.remove(creature)


@dataclass
class door:
    """
    doors
    """

    def __init__(self, location, to, to_location):
        self.location = location
        self.to = to
        self.to_location = to_location


@dataclass
class potion:
    """
    Potions
    """

    def __init__(self, name, effect, potency, size, m):
        self.name = name
        self.effect = effect #str
        self.potency = potency #int
        self.size = size #int

    def use(self, player):
        if self.effect == "health":
            player.current_health += self.potency

        self.size -= 1

        if self.size == 0:
            player.display_inventory.remove(self.name)
            player.inventory.remove(self)
            print("You take a final sip and cast aside the empty bottle")
            return

        print("You gulp down a portion of the fluid in the bottle. You can tell you have around " + str(self.size) + " good sips left before the bottle is empty.")

def roll(sides):
    result = random.randrange(1, sides + 1)
    return result


def combat(combatant1, combatant2, prev_action):
    """
    Basic Combat
    WiP: Body Part Targeting, Shields(Block), Status Effects, Item Usage, Varying Enemy AI
    """
    if combatant1.health > 0 and combatant2.health > 0 and prev_action != "run":  # If both combatants are still alive
        if isinstance(combatant1, player):  # if the combatant is a player
            # Check up on the player hp
            print("HP:" + str(combatant1.current_health))
            # Ask the player what they would like to do
            action = input(
                "What would you like to do?(Attack/Parry/Dodge/Inspect/Run)").lower()
            if action == "attack":  # Attack
                if combatant1.equipped_wep.mod + combatant1.wep_exp[combatant1.equipped_wep.typ] // 100 + roll(20) < combatant2.equipped_armor.AC:
                    print("Your blow bounces off their armor!")
                    combatant1.wep_exp[combatant1.equipped_wep.typ] += (
                        roll(combatant1.equipped_wep.damage_die)) // 2
                    combat(combatant2, combatant1, action)
                else:
                    combatant1.equipped_wep.attack(combatant2, combatant1)
                    combat(combatant2, combatant1, action)

            elif action == "inspect":  # Inspect
                combatant2.inspect()
                combat(combatant1, combatant2, action)

            elif action == "parry":
                print("You prepare to parry the next attack")
                combat(combatant2, combatant1, action)

            elif action == "dodge":
                print("You prepare to dodge the next attack")
                combat(combatant2, combatant1, action)

            elif action == "run":  # Run
                print("You Flee!")
                return

            else:  # Idiotproofing
                print("Please input a valid command!")
                combat(combatant1, combatant2, None)

        else:  # Basic enemy attacking AI
            action = "attack"

            if prev_action == "parry" and action == "attack":
                if combatant1.equipped_wep.mod + roll(20) < combatant2.equipped_armor.AC:
                    print("Their blow bounces off your armor!")
                    combat(combatant2, combatant1, action)
                else:
                    combatant1.equipped_wep.parry(combatant2, combatant1)
                    combat(combatant2, combatant1, action)

            elif prev_action == "dodge" and action == "attack":
                if combatant1.equipped_wep.mod + roll(20) < combatant2.agility + roll(20) - (combatant2.equipped_wep.weight + combatant2.equipped_armor.weight):
                    print("You manage to dodge the blow!")
                    combat(combatant2, combatant1, action)
                else:
                    print("You can't dodge fast enough!")
                    combatant1.equipped_wep.attack(combatant2, combatant1)
                    combat(combatant2, combatant1, action)

            elif action == "attack":
                if combatant1.equipped_wep.mod + roll(20) < combatant2.equipped_armor.AC:
                    print("Their blow bounces off your armor!")
                    combat(combatant2, combatant1, action)
                else:
                    combatant1.equipped_wep.attack(combatant2, combatant1)
                    combat(combatant2, combatant1, action)

    else:  # End of combat
        if isinstance(combatant2, player):
            print(combatant1.name + " has Died")
            loot = combatant1.loot()
            for item in loot:
                combatant2.inventory += [item]
                combatant2.display_inventory += [item.name.strip('"')]
            combatant2.get_xp(combatant1.exp)
            return combatant1

        else:
            print(combatant2.name + " has Died")
            loot = combatant2.loot()
            for item in loot:
                combatant1.inventory += [item]
                combatant1.display_inventory += [item.name.strip('"')]
            combatant1.get_xp(combatant2.exp)
            return combatant1
