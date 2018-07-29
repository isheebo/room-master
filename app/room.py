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

    def is_empty(self):
        return len(self.members) == 0

    def is_full(self):
        return len(self.members) >= self.capacity

    def available_spaces(self):
        return self.capacity - len(self.members)

    def add_person(self, person):
        """
        adds a person to a room that is not yet filled up
        """
        person.type == 'Fellow' and self._add_fellow(
            person) or person.type == 'Staff' and self._add_staff(person)

    def _add_fellow(self, fellow):
        if not self.is_full():
            self.members.append(fellow)
            return True
        return False

    def _add_staff(self, staff):
        if not self.is_full():
            self.members.append(staff)
            return True
        return False

    def __repr__(self):
        return f"{self.name.title()}"

    def __str__(self):
        return f"{self.name.title()}"
