"""
Module for representing a die.
"""

import random


class Die:
    """
    Represents one die in the game of Yahtzee.
    """

    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6

    def __init__(self, value=None):
        """
        New die with a random value or the specified value.

        Args:
            value (int, optional): The value of the die. Defaults to None.
        """
        if value is None:
            self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)
        elif value > self.MAX_ROLL_VALUE:
            self._value = self.MAX_ROLL_VALUE
        elif value < self.MIN_ROLL_VALUE:
            self._value = self.MIN_ROLL_VALUE
        else:
            self._value = value

    def get_name(self):
        """
        Returns the word for the die's value.

        Returns:
            str: The word of the value.
        """
        names = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}
        return names.get(self._value, "unknown")

    def get_value(self):
        """
        Gives the value of the die.

        Returns:
            int: The value of the die.
        """
        return self._value

    def roll(self):
        """
        Rolls the die and updates its value.
        """
        self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)

    def __str__(self):
        """
        Returns the string representation of the die.

        Returns:
            str: The string representation of the die.
        """
        return str(self._value)
