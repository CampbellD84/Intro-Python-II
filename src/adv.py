from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name_of_player = input("Please enter your name: ")
new_player = Player(name_of_player, "outside")
# Write a loop that:
while True:
    # * Prints the current room name
    # print(new_player.curr_location)
    # * Prints the current description (the textwrap module might be useful here).
    print(room['outside'].room_desc)
    # * Waits for user input and decides what to do.
    move_to_new_room = input(
        "Please select a direction\
            (n)orth, (s)outh, (e)ast, or (w)est Or q(uit): ").lower()

    # If the user enters a cardinal direction, attempt to move to the room there.
    if move_to_new_room == "n":
        if room[new_player.curr_location].n_to:
            new_player.curr_location = room[new_player.curr_location].n_to
            print(f'{new_player.curr_location}')
        elif not room[new_player.curr_location].n_to:
            print("Cannot go north! Choose another direction.")
    elif move_to_new_room == "s":
        if room[new_player.curr_location].s_to:
            new_player.curr_location = room[new_player.curr_location].s_to
            print(f'{new_player.curr_location}')
        elif not room[new_player.curr_location].s_to:
            print("Cannot go south! Choose another direction.")
    elif move_to_new_room == "w":
        if room[new_player.curr_location].w_to:
            new_player.curr_location = room[new_player.curr_location].w_to
            print(f'{new_player.curr_location}')
        elif not room[new_player.curr_location].w_to:
            print("Cannot go west! Choose another direction.")
    elif move_to_new_room == "e":
        if room[new_player.curr_location].e_to:
            new_player.curr_location = room[new_player.curr_location].e_to
            print(f'{new_player.curr_location}')
        elif not room[new_player.curr_location].e_to:
            print("Cannot go east! Choose another direction.")
    elif move_to_new_room == "q":
        # If the user enters "q", quit the game.
        False
        exit()
    else:
        # Print an error message if the movement isn't allowed.
        print("Command not recognized. Please select n,s,e,w or q. ")
