"""
Beastiary.py
Contains all of the monster classes for the game
To Do: Enemy Generation, Loot Tables, Enemy Sentience
"""
import random
import mechanics
from dataclasses import dataclass

@dataclass
class monster:
    def __init__(self, name, inventory, equipped_wep, equipped_armor, current_location, aggro):
        self.name = name
        self.health = random.randrange(10, 20)
        self.inventory = inventory
        self.equipped_wep = equipped_wep
        self.equipped_armor = equipped_armor
        self.exp = random.randrange(25, 75, 5)
        self.level = 2
        self.agility = random.randrange(5, 8)
        self.status = None
        self.current_location = current_location
        self.aggro = aggro

    def loot(self):
        if self.health > 0:
            print("This creature is still alive!")
            return None
        else:
            print("The spoils of war are yours!")
            return self.inventory

    def inspect(self):
        print("\n" + self.name + ":\n" + "Health: " + str(self.health) + "\n" + "Equipped Weapon: " + self.equipped_wep.name
              + "\n" + "Equipped Armor: " + self.equipped_armor.name + "\n" + "Level: " + str(self.level))

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
class goblin:

    def __init__(self, name, inventory, equipped_wep, equipped_armor, current_location):
        monster.__init__(self, name, inventory, equipped_wep, equipped_armor, current_location, 5)
        self.health = random.randrange(10, 20)
        self.exp = random.randrange(25, 75, 5)
        self.level = 2
        self.agility = random.randrange(5, 8)
        self.status = None

    def loot(self):
        if self.health > 0:
            print("This creature is still alive!")
            return None
        else:
            print("The spoils of war are yours!")
            self.inventory += [self.equipped_wep]
            self.inventory += [self.equipped_armor]
            return self.inventory

    def inspect(self):
        print("\n" + self.name + ":\n" + "Health: " + str(self.health) + "\n" + "Equipped Weapon: " + self.equipped_wep.name
              + "\n" + "Equipped Armor: " + self.equipped_armor.name + "\n" + "Level: " + str(self.level))
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
class goblin_king:

    def __init__(self, name, inventory, equipped_wep, equipped_armor, current_location):
        monster.__init__(self, name, inventory, equipped_wep, equipped_armor, current_location, 3)
        self.health = random.randrange(30, 50)
        self.exp = random.randrange(100, 300, 25)
        self.level = 4
        self.agility = random.randrange(3, 5)

    def loot(self):
        if self.health > 0:
            print("This creature is still alive!")
            return None
        else:
            print("The spoils of war are yours!")
            self.inventory += [self.equipped_wep]
            self.inventory += [self.equipped_armor]
            return self.inventory

    def inspect(self):
        print("\n" + self.name + ":\n" + "Health: " + str(self.health) + "\n" + "Equipped Weapon: " + self.equipped_wep.name
              + "\n" + "Equipped Armor: " + self.equipped_armor.name + "\n" + "Level: " + str(self.level))

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
class hound:

    def __init__(self, name, inventory, equipped_wep, equipped_armor, current_location):
        monster.__init__(self, name, inventory, equipped_wep, equipped_armor, current_location, 3)
        self.health = random.randrange(8, 12)
        self.exp = random.randrange(50, 150, 25)
        self.level = 2
        self.agility = random.randrange(5, 8)

    def loot(self):
        if self.health > 0:
            print("This creature is still alive!")
            return None
        else:
            print("The spoils of war are yours!")
            self.inventory += [self.equipped_wep]
            self.inventory += [self.equipped_armor]
            return self.inventory

    def inspect(self):
        print("\n" + self.name + ":\n" + "Health: " + str(self.health) + "\n" + "Equipped Weapon: " + self.equipped_wep.name
              + "\n" + "Equipped Armor: " + self.equipped_armor.name + "\n" + "Level: " + str(self.level))

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
