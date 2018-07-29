class Person:
    def __init__(self, name, wants_accommodation=False):
        self.name = name
        self.wants_accommodation = False
        self.type = self.__class__.__name__
