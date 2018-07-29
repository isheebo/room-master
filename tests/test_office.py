import unittest

from app.fellow import Fellow
from app.office import Office
from app.staff import Staff


class OfficeTest(unittest.TestCase):
    def setUp(self):
        self.office = Office('Blue')
        self.staff1 = Staff('Will')

    def test_office_has_max_capacity_six(self):
        self.assertEqual(self.office.capacity, 6)

    def test_office_properties(self):
        self.assertEqual(self.office.name, 'Blue')
        self.assertEqual(self.office.type, 'Office')

    def test_no_members_yet(self):
        self.assertEqual(len(self.office.members), 0)

    def test_assert_office_is_not_full(self):
        self.assertFalse(self.office.is_full())
        self.assertTrue(self.office.is_empty())

    def test_office_can_accept_person_objects(self):
        self.office.add_person(self.staff1)
        self.assertFalse(self.office.is_empty())
        self.assertFalse(self.office.is_full())
        self.assertEqual(self.office.available_spaces(), 5)

    def test_office_can_fill_up(self):
        self.office.add_person(Staff('Atukwase Sylvestre'))
        self.office.add_person(Staff('Murungi Patricia'))
        self.office.add_person(Fellow('Patience Mukami', True))
        self.office.add_person(Staff('Irene Mulyagonja'))
        self.office.add_person(Staff('Annie Myles'))
        self.office.add_person(Staff('John Katureebe'))
        self.office.add_person(Staff('George Williams'))

        self.assertEqual(len(self.office.members), 6)
        self.assertTrue(self.office.is_full())

    def test_add_person_in_available_room(self):
        response = self.office.add_person(Fellow('Kadongo Moses'))
        self.assertTrue(response)
