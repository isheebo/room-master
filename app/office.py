from app.room import Room
from app.fellow import Fellow
from app.staff import Staff
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
        super(Office, self).__init__(name, 6)

    def add_person(self, name, person_type):
        """
        adds a person to a room that is not yet filled up
        """
        person_type == 'Fellow' and self._add_fellow(
            name) or person_type == 'Staff' and self._add_staff(name)

    def _add_fellow(self, name, wants_accommodation):
        fellow = Fellow(name, wants_accommodation)

        if not self.is_full():
            self.members.append(fellow)
            return True

        return False

    def _add_staff(self, name):
        staff = Staff(name)

        if not self.is_full():
            self.members.append(staff)
            return True

        return False
