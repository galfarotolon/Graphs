from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

## from utils import Stack, Queue, Graph


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
------------------------
Traverse the whole graph and store mapped world in dict

Helper function to get each room exit, and setting each
room direction to ? before being visited, only change it
after doing so

Helper function to traverse map, changing the player current location to match the 
room currently in
- Check the directions available, if not visited yet, visit it and make corresponding changes
(i.e remove from unvisited arr and addd it to visited)
- make sure to get bi-directions set up and opposites (n:s, s:n and so on)
- check if the new room entered is already saved in the world map, if its not, check all possible
  exits and update the results

Helper function that checks all rooms with '?' by going to the opposite paths
of the rooms visited, 
 - make corresponding changes (remove from opposite paths arr  and add it to the 
    traversed paths arr)

 - conditions
 - while the world map is smaller than the total number of rooms (500), 
    check the initial room

- if the new room is not in the world map
    get all the room's exits 

- for all directions and rooms,
    if the room has an unvisited direction (i.e ?)
    add it to the list of unvisited directions

- as long as there are unvisited paths, keep traversing the map

- similarly, check all the opposite paths for missing directions

- get all room exits of the current rooms by picking random directions
  available and making the player travel there, repeat process until
   all rooms and their opposite directions have been mapped out


'''

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt" -- PASSING: 2 moves / 3 rooms visited
# map_file = "maps/test_cross.txt" -- PASSING: 14 moves / 9 rooms visited
# map_file = "maps/test_loop.txt" -- PASSING: 16 moves / 12 rooms visited (its possible to get down to 14 moves)
# map_file = "maps/test_loop_fork.txt" -- PASSING: 28 moves / 18 rooms visited (its possible to get fewer, around 24)
map_file = "maps/main_maze.txt" 
# -- PASSING: 1004 moves / 500 rooms visited

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
    # and remove it since direction will become visited
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


# go back to all the rooms that have '?' in their directions
def check_missing_directions(room):
    # check the list last items
    # loop through paths in opposite_path arr
    for direction in opposite_path[-1]:

        # the player travels to one of the rooms with a '?'
        player.travel(direction)

        # add it to the traversal path
        traversal_path.append(direction)
        
        #in the same way, now remove it from the oppsite_path arr
        opposite_path.pop(-1)

        # if the current room being checked has a '?' in any of its directions.
        # return it
        # check only the values of the world map dict
        if '?' in world_map[player.current_room.id].values():
            return



## Main Traversal logic

# while the length of the world map is smaller than the total number
# of rooms in the world

# while len(world_map) < 500:
while len(world_map) < len(room_graph):
    # start the player in the default current room
    new_room = player.current_room

    #check to see if that room is in the world map
    if new_room.id not in world_map:
        # if it isnt, get all the available exits from the room
        get_room_exits(new_room)
    
    # keep an array storing all unvisited paths
    unvisited_paths = []

    # for all the directions and rooms in the new room visited:
    for direction, room in world_map[new_room.id].items():

        # if the room has '?', add it to the unvisited paths arr
        if room == '?':
            unvisited_paths.append(direction)

    # traverse the map by checking all the unvisited_paths
    # per room

    # as long as there are unvisited paths
    if len(unvisited_paths) > 0:
        traverse_map(new_room, unvisited_paths)
    else:
        # (BFS) find closest rooms with '?' in direction to
        # go through
        if len(opposite_path) > 0:
            check_missing_directions(new_room)

        else:
            # get all the exits of  the room
            exits = new_room.get_exits()

            # choose a random direction to go through
            random_direction = random.choice(exits)

            # traverse the player to the new random direction
            player.travel(random_direction)

    





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
