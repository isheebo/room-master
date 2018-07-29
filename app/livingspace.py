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
