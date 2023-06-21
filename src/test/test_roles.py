import unittest
from roles import Mafia, Detective, Doctor, Townsfolk


class TestRoles(unittest.TestCase):
    def test_roles(self):
        self.assertEqual(Mafia().name, "Mafia")
        self.assertEqual(Detective().name, "Detective")
        self.assertEqual(Doctor().name, "Doctor")
        self.assertEqual(Townsfolk().name, "Townsfolk")

    # Add more tests as necessary...


if __name__ == "__main__":
    unittest.main()
