import random
from app.fellow import Fellow
from app.staff import Staff


class Amity:
    def __init__(self):
        self.employees = []
        self.available_offices = []
        self.available_livingspaces = []

    def add_person(self, name, person_type, wants_accommodation):
        """
        adds a newly *inducted* person into the room allocation system.
        It can go ahead and grant them rooms depending on their person type.
        """
        person = None
        if person_type == 'Fellow':
            person = Fellow(name, wants_accommodation)
        elif person_type == 'Staff':
            person = Staff(name)
        else:
            print("unknown person type: expecting <Fellow> or <Staff> type")
            return False

        if person is not None:
            self.employees.append(person)
            self.allocate_person_room(person)
        return True

    def allocate_person_room(self, person):
        """
        Assumes that we have some rooms available to the system.
        Allocates a newly created person a room basing on their person type.
        """
        office = random.choice(self.available_offices)
        office.add_person(person)

        if person.type == 'Fellow' and person.wants_accommodation:
            livingspace = random.choice(self.available_livingspaces)
            livingspace.add_person(person)
