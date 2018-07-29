class Person:
    def __init__(self, name, wants_accommodation=False):
        self.name = name
        self.wants_accommodation = wants_accommodation
        self.type = self.__class__.__name__
