import unittest
from game import Game


class TestGame(unittest.TestCase):
    def test_assign_roles(self):
        game = Game(["Alice", "Bob", "Charlie", "Dave"])
        self.assertEqual(len(game.players), 4)

    # Add more tests as necessary...


if __name__ == "__main__":
    unittest.main()
