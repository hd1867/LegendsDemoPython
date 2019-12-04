"""
An RPing application
"""

import mechanics
from armory import *
from beastiary import *
from world import *


def birth(name):
    """
    Creates a base player with no items, inventory, armor, and slightly varying stats
    """
    return mechanics.player(name, random.randrange(10, 15), [], unarmed, human_skin, 0, 1, 3)




def populate(env, player):
    directions = ["north", "south", "east", "west", "northeast",
                  "northwest", "southeast", "southwest", "still"]
    eastwall = ["north", "south", "west", "northwest", "southwest"]
    westwall = ["north", "south", "east", "northeast", "southeast"]
    northwall = ["south", "east", "west", "southeast", "southwest"]
    southwall = ["north", "east", "west", "northeast", "northwest"]
    for creature in env.present:
        if creature.name != player.name:
            if is_within(creature, player):
                move_towards(creature, player)
            else:
                if creature.current_location.x + 1 >= env.width:
                    creature.move(southwall[random.randrange(0, 5)])
                    print(creature.name + " hit southwall")
                if creature.current_location.x - 1 <= 0:
                    creature.move(northwall[random.randrange(0, 5)])
                    print(creature.name + " hit northwall")
                if creature.current_location.y + 1 >= env.height:
                    creature.move(eastwall[random.randrange(0, 5)])
                    print(creature.name + " hit westwall")
                if creature.current_location.y - 1 < 0:
                    creature.move(westwall[random.randrange(0, 5)])
                    print(creature.name + " hit eastwall")
                else:
                    creature.move(directions[random.randrange(0, 9)])


def move_towards(creature, target):
    if target.current_location.x > creature.current_location.x:
        creature.current_location.x += 1
    if target.current_location.x < creature.current_location.x:
        creature.current_location.x -= 1
    if target.current_location.y > creature.current_location.y:
        creature.current_location.y += 1
    if target.current_location.y < creature.current_location.y:
        creature.current_location.y -= 1


def is_within(creature, target):
    return (abs(creature.current_location.x - target.current_location.x) <= creature.aggro) or (abs(creature.current_location.y - target.current_location.y) <= creature.aggro)


def combat_trigger(env, player):
    for creature in env.present:
        if player.current_location.x == creature.current_location.x and player.current_location.y == creature.current_location.y:
            if creature.name != player.name:
                print("\nYou have encountered " +
                      creature.name + " prepare for combat! \n")
                combat(player, creature, "Move")
                env.present.remove(creature)
                player.inspect()


def door_trigger(env, player):
    for door in env.doors:
        if player.current_location.x == door.location.x and player.current_location.y == door.location.y:
            traverse = input(
                "Would you like to go through the door?(Y/N)").lower()
            if traverse == "y":
                door.to.recieve(player, env, door)
                player.current_location = door.to_location
                return door.to

    return env


def navigate(env, player):

    print("\n")
    env.chart()
    dire = input("What direction would you like to move in?\n").lower()
    player.move(dire)
    combat_trigger(env, player)
    populate(env, player)
    combat_trigger(env, player)
    env.chart()

    return door_trigger(env, player)


def game(env, player):
    while player.current_health > 0:
        print(env.doors)
        env.chart()
        action = input("What would you like to do?\n").lower()
        if action == "move":
            env = navigate(env, player)
        if action == "inspect":
            player.inspect()
        if action == "equip":
            print(player.display_inventory)
            item = input("What would you like to equip?\n")
            if item in player.display_inventory:
                for equipment in player.inventory:
                    if equipment.name == item:
                        player.equip(equipment)
            else:
                print("You don't have this item!")
        if action == "help":
            pass
        if action == "exit":
            return

    print("You have DIED!")


game(field, holanow)
