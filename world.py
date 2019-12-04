"""
world.py
The map of the world for the game, all of the environments, enemies, dungeongen, and doors
"""

import mechanics
from armory import *
from beastiary import *

holanow = mechanics.player("Holanow", 75, [], [], moonlight_horn, stone_mail, 1999, 5, 10, mechanics.point(0, 0))

################################################################################
#Goblin Cave Test Module
#Rooms: 10
#Enemies: Goblins, Palixtpaz, Dragon?, Hounds
#Levels: 5-7?
################################################################################

palixtpaz = goblin_king("Palixtipaz", [], superior_penetrator,
                        goblinhide_chestplate, mechanics.point(5, 7))
goblin1 = goblin("Goblin", [], scimitar, goblin_skin, mechanics.point(
    random.randrange(2, 8), random.randrange(2, 8)))

goblin2 = goblin("Goblin", [], whip, goblin_skin, mechanics.point(
    random.randrange(2, 8), random.randrange(2, 8)))

goblin3 = goblin("Goblin", [], scimitar, goblin_skin, mechanics.point(
    random.randrange(2, 8), random.randrange(2, 8)))

goblin4 = goblin("Goblin", [], scimitar, goblin_skin, mechanics.point(
    random.randrange(2, 8), random.randrange(2, 8)))

hound1 = hound("Hound", [], lesser_beast_fangs, lesser_beast_hide, mechanics.point(
    random.randrange(1, 9), random.randrange(2, 8)))

hound2 = hound("Hound", [], lesser_beast_fangs, lesser_beast_hide, mechanics.point(
    random.randrange(1, 9), random.randrange(2, 8)))

hound3 = hound("Hound", [], lesser_beast_fangs, lesser_beast_hide, mechanics.point(
    random.randrange(1, 9), random.randrange(2, 8)))

hound4 = hound("Hound", [], lesser_beast_fangs, lesser_beast_hide, mechanics.point(
    random.randrange(1, 9), random.randrange(2, 8)))

hound5 = hound("Hound", [], lesser_beast_fangs, lesser_beast_hide, mechanics.point(
    random.randrange(1, 9), random.randrange(2, 8)))

hound6 = hound("Hound", [], lesser_beast_fangs, lesser_beast_hide, mechanics.point(
    random.randrange(1, 9), random.randrange(2, 8)))

hound7 = hound("Hound", [], lesser_beast_fangs, lesser_beast_hide, mechanics.point(
    random.randrange(1, 9), random.randrange(2, 8)))

#The second room of the cave
kennel_door_inner = mechanics.door(point(12, 3), "cave", point(0,3))
kennel = mechanics.environment("Goblin Kennel", 12, 20, [hound1, hound2, hound3, hound4, hound5, hound6, hound7, goblin1, goblin2],
                               "Darkness", [], [])


#The first room of the cave
cave_door_inner_1 = mechanics.door(point(5, 0), "field", point(0,5))
cave_door_inner_2 = mechanics.door(point(4, 0), "field", point(0,4))
cave = mechanics.environment("Cave Entrance", 10, 10, [
                             goblin1, goblin2, goblin3], "Darkness", [cave_door_inner_1, cave_door_inner_2], [])

kennel_door_outer = mechanics.door(point(0,3), kennel, point(12, 3))
kennel_door_inner.to = cave 
#The field outside the cave
cave_door_outer_1 = mechanics.door(point(0, 4), cave, point(5, 0))
cave_door_outer_2 = mechanics.door(point(0, 5), cave, point(4, 0))
field = mechanics.environment("Goblin Fields", 8, 12, [
                              holanow, goblin1], "None", [cave_door_outer_1, cave_door_outer_2], [])

cave_door_inner_1.to = field
cave_door_inner_2.to = field
