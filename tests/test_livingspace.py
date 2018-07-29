import unittest

from app.fellow import Fellow
from app.livingspace import LivingSpace
from app.staff import Staff


class TestLivingSpace(unittest.TestCase):
    def setUp(self):
        self.livingspace = LivingSpace('Zanzibar')

    def test_livingspace_properties(self):
        self.assertEqual(self.livingspace.type, 'LivingSpace')
        self.assertEqual(self.livingspace.capacity, 4)
        self.assertEqual(self.livingspace.name, 'Zanzibar')

    def test_staff_not_added_to_livingspaces(self):
        self.assertEqual(len(self.livingspace.members), 0)
        resp = self.livingspace.add_person(Staff('Kadongo Moses'))
        self.assertEqual(len(self.livingspace.members), 0)
        self.assertFalse(resp)
        self.assertTrue(self.livingspace.is_empty())

    def test_no_space_for_no_accommodation(self):
        response = self.livingspace.add_person(
            Fellow('Kadongo Moses', wants_accommodation=False))
        self.assertFalse(response)

    def test_add_fellow_that_needs_accommodation(self):
        response = self.livingspace.add_person(
            Fellow('Kadongo Moses', wants_accommodation=True))
        self.assertTrue(response)

    def test_cannot_exceed_capacity_4_per_room(self):
        self.livingspace.add_person(
            Fellow('Kadongo Moses', wants_accommodation=True))
        self.livingspace.add_person(
            Fellow('Kawalya Jr', wants_accommodation=True))
        self.livingspace.add_person(
            Fellow('Natalie Jones', wants_accommodation=True))
        self.livingspace.add_person(
            Fellow('Mariam Ndagire', wants_accommodation=True))

        self.assertEqual(len(self.livingspace.members), 4)
        self.assertTrue(self.livingspace.is_full())

        self.livingspace.add_person(
            Fellow('Teacher Mpamire', wants_accommodation=True))

        self.assertEqual(len(self.livingspace.members), 4)
