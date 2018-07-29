from app.person import Person


class Fellow(Person):
    def __init__(self, name, wants_accommodation=False):
        super(Fellow, self).__init__(name, wants_accommodation)
        self.office_space = None  # connection to Office space
        self.living_space = None  # connection to the LivingSpace
