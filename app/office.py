from app.room import Room
# big question is: At what stage do we really need to create a person?
# do we create a person when we are creating a room or we create a
# person when we are adding them to the system.
#
# Once a new person comes in, create them first, add them to the list
# of either staff or fellows.
# Then after adding them, see if there are rooms that can accommodate them,
# If there are, add them to those rooms.
# otherwise let them count as the unallocated.


class Office(Room):
    def __init__(self, name):
        self.capacity = 6
        super(Office, self).__init__(name, self.capacity)
