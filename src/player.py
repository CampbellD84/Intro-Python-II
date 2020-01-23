# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, player_name, curr_location):
        self.player_name = player_name
        self.curr_location = curr_location

    def __str__(self):
        return str(self.__dict__)
