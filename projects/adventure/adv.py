from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from utils import Stack, Queue, Graph

# Load world
world = World()




# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "test_line.txt"
# map_file = "test_cross.txt"
# map_file = "test_loop.txt"
# map_file = "test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

'''
Ideas: 

initialize a dict to map all the world
initialize a set with all visited rooms

- create a dict to store opposite-directions(i.e n - s, e - w)
- store oppositepath in array

Travel in a single direction until there are no
more exits. Continue by looking for the closest vertex that has a missing direction 
(represented by ? in each room direction) 
travel in that missing direction for as long as possible. 
Switch directions and do the same thing
--
Traverse the whole graph and store mapped maze in dict


'''

world_map = {}

# Make sure opposite directions are covered both ways (ie n:s and s:n)
opposite_directions = {'n': 's', 's':'n', 'w' : 'e', 'e' : 'w'}


# Get all room exists from Room class method





# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
