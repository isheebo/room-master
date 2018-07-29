from app.room import Room


class Office(Room):
    def __init__(self, name):
        super(Office, self).__init__(name, 6)
