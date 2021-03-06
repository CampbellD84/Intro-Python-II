from room import Room
from player import Player
from item import Item


# Declare Items
sword = Item("Sword", "An ancient samurai sword.")
helmet = Item("Helmet", "Helmet created by demons.")
armor = Item("Armor", "Special armor made from dragon scales.")
boots = Item("Boots", "Boots with power of flight and super speed.")


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


# Place Items in Room
room['treasure'].rm_items = [armor, sword]
room['narrow'].rm_items = [helmet]
room['foyer'].rm_items = [boots]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


def check_direction(direction, curr_room):
    rm = direction + '_to'
    if hasattr(curr_room, rm):
        return getattr(curr_room, rm)

    elif direction == "q":
        # If the user enters "q", quit the game.
        print("Thanks for playing!")
        exit()

    # elif direction == "get":
    #     take_rm_item(new_player, curr_room)

    else:
        print('Cannot proceed in that direction')
        return curr_room


def check_room_items(curr_rm):
    if len(curr_rm.rm_items) > 0:
        return f'Items in room: {[itm.item_name for itm in curr_rm.rm_items]}'
    else:
        return f'No Items in room.'


def take_rm_item(player, curr_rm):
    for itm in curr_rm.rm_items:
        player.items_found.append(itm.item_name)
        curr_rm.rm_items.clear()
        return player.get_inventory()


name_of_player = input("Please enter your name: ")
new_player = Player(name_of_player, room['outside'], items_found=[])

# Write a loop that:
while True:
    # * Prints the current room name
    print(f'{new_player.player_name}, you are in {new_player.curr_location.name}. {new_player.curr_location.room_desc}')
    print(check_room_items(new_player.curr_location))
    print(new_player.get_inventory())
    print(check_room_items(new_player.curr_location))

    # * Waits for user input and decides what to do.
    move_to_new_room = input(
        "Please select a direction\
            n, s, e, w, get Or q: ").lower()

    new_player.curr_location = check_direction(
        move_to_new_room, new_player.curr_location)

    new_player.items_found = take_rm_item(
        new_player, new_player.curr_location)

    items_in_room = check_room_items(new_player.curr_location)
