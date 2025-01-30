"""
Unit tests for the Hand class.
"""

import unittest
import random
import sys
from src.die import Die

sys.path.append("..")

class TestDie(unittest.TestCase):
    """
    Unit tests for the Die class.
    """

    def test_no_argument(self):
        """
        Test that a new die is created with a random value between 1 and 6.
        """
        random.seed(1)
        die = Die()
        self.assertEqual(die.get_value(), 2)

    def test_with_argument(self):
        """
        Test that a new die is created with the specified value.
        """
        die = Die(4)
        self.assertEqual(die.get_value(), 4)

    def test_with_invalid_argument(self):
        """
        Test that a die created with an invalid value defaults to 6.
        """
        die = Die(100)
        self.assertEqual(die.get_value(), 6)

    def test_roll(self):
        """
        Test that rolling the die updates its value to a new random number.
        """
        random.seed(1)
        die = Die()
        die.roll()
        self.assertEqual(die.get_value(), 5)

    def test_get_name(self):
        """
        Test that the name of the die matches the correct value-to-name mapping.
        """
        die = Die(3)
        self.assertEqual(die.get_name(), "three")


if __name__ == "__main__":
    unittest.main()
