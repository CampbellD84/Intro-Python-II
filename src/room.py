# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, room_desc):
        self.name = name
        self.room_desc = room_desc

    def __str__(self):
        return f'Welcome to {self.name}.  {self.room_desc}'
