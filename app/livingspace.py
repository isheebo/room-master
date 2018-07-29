from app.room import Room


class LivingSpace(Room):
    def __init__(self, name):
        self.capacity = 4
        super(LivingSpace, self).__init__(name, self.capacity)

    def _add_staff(self, staff):
        """
        Since staff cannot be allocated livingspaces
        """
        return False

    def _add_fellow(self, fellow):
        if not self.is_full() and fellow.wants_accommodation:
            self.members.append(fellow)
            return True
        return False
