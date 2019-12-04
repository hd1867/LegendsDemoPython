"""
Armory.py
All of the weapons, armor, adn shields for the game
"""

from mechanics import *


################################################################################
#Weapons
################################################################################
moonlight_horn = weapon("Moonlight Horn", "Spear", 12, "arcane", 2, 3)

scimitar = weapon("Scimitar", "Sword", 6, "slashing", 0, 1)

superior_penetrator = weapon("Superior Penetrator", "Spear", 11, "piercing", 2, 4)

unarmed = weapon("Hand", "Martial", 1, "bludgeoning", 0, 0)

lesser_beast_fangs = weapon("Lesser Beast Fang", "Animal", 6, "piercing", 1, 0)

whip = weapon("Whip", "Flail", 8, "slashing", 2, 1)
################################################################################
#Armor
################################################################################
stone_mail = armor("Stone Mail", 12, 300, 10)

goblin_skin = armor("Goblin Skin", 8, 50, 0)

goblinhide_chestplate = armor("Goblinhide Chestplate", 9, 100, 3)

human_skin = armor("Skin", 5, 10000, 0)

lesser_beast_hide = armor("Lesser Beast Hide", 6, 10000, 0)
################################################################################
#Potions
################################################################################
#minor_health_potion = potion("Minor Health Potion", "health", 5, 3)

#esser_health_potion = potion("Lesser Heath Potion", "health", 10, 3)

#health_potion = potion("Health Potion", "health", 20, 3)

#greater_health_potion = potion("Greater Health Potion", "health", 50, 3)

#supreme_health_potion = potion("Supreme Health Potion", "health", 100, 3)

#lyneera_flask = potion("Flask of Lyneera", "health", 125, 9999)
