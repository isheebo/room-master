import unittest
from app.office import Office
from app.staff import Staff


class OfficeTest(unittest.TestCase):
    def setUp(self):
        self.office = Office('Blue')
        self.staff1 = Staff('Will')

    def test_office_has_max_capacity_six(self):
        self.assertEqual(self.office.capacity, 6)

    def test_office_name(self):
        self.assertEqual(self.office.name, 'Blue')

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
        self.office.add_person(Staff('Irene'))
        self.office.add_person(Staff('Annie'))
        self.office.add_person(Staff('George'))
        self.office.add_person(Staff('Irene'))
        self.office.add_person(Staff('Annie'))
        self.office.add_person(Staff('George'))
        self.office.add_person(Staff('George'))
        self.assertEqual(len(self.office.members), 6)
        self.assertTrue(self.office.is_full())
