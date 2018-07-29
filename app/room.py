class Room:
    """
    Defines the Room class.
    :params
    name: string, the name of a room
    capacity: Integer, the maximum capacity of a room
    """

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.members = []  # list of people occupying a particular room
        self.type = self.__class__.__name__  # type of the class

    def is_full(self):
        return len(self.members) >= self.capacity

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"
