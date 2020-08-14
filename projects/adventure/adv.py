from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from utils import Stack, Queue, Graph


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

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
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


# initialize a dict to map all the world
world_map = {}

# Make sure opposite directions are covered both ways (ie n:s and s:n)
opposite_directions = {'n': 's', 's':'n', 'w' : 'e', 'e' : 'w'}

#store opposite path in array
opposite_path = []

# initialize visited rooms set
visited_rooms = set()


# Get all room exists from Room class method

def get_room_exits(room):
    # create a dict for the room by using the room Id
    world_map[room.id] = {}
    # get all the exits for each room
    room_exits = room.get_exits()
    # loop through each room exit
    for room_exit in room_exits:
        # store all the '?'s to indicate direction
        # not yet visited, as the direction values
        # for n,s,e,w 
        world_map[room.id][room_exit] = '?'


# Traverse the map, moving from room to room and saving directions
# (also save bi direction)
# check opposite directions

def traverse_map(room, directions):
    # prev room traversed is current player location
    prev_room  = player.current_room.id 

    # get new direction from directions available
    # and remove it since direction will come visited
    new_direction = directions.pop(0)

    # move the player into new room/direction
    player.travel(new_direction)

    # new room id becomes player new current room id
    new_room_id = player.current_room.id
    new_room = player.current_room

    # add the direction that was just traveled to the
    # traversal path list
    traversal_path.append(new_direction)

    # get the reverse direction saved as well
    # i.e. if you move from room 1 to 2 by going north,
    # then its  the same as going from room 2 to 1 going south
    bi_directional = opposite_directions.get(new_direction)

    # add that bi_directional to the opposite path array
    # this way world map is mapped quicker by adding
    # both paths each time a traversal to a new room is made

    opposite_path.append(bi_directional)

    # check if the new room entered is already in world map
    if new_room_id not in world_map:

        # get all the possible room exits
        get_room_exits(new_room)

        # update the previous rooms inserted in the world map
        world_map[prev_room][new_direction] = new_room_id

        # update the new rooms inserted in the world map
        world_map[new_room_id][bi_directional] = prev_room

    else:
        # update the world map listing
        world_map[prev_room][new_direction] = new_room_id






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
