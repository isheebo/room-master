from app.person import Person


class Staff(Person):
    def __init__(self, name):
        super(Staff, self).__init__(name)
        self.office_space = None  # connection to the Office space room
