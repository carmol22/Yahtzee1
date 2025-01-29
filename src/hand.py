"""
Module for representing a hand of dice.
"""

from src.die import Die


class Hand:
    """
    Represents a hand of dice.
    """

    def __init__(self, dice_values=None):
        """
        A new hand of dice within the range of 1 to 6.

        Args:
            dice_values (list, optional): The values of the dice. Defaults to None.
        """
        if dice_values is None:
            self.dice = []
            for _ in range(5):
                self.dice.append(Die())
        else:
            self.dice = []
            for value in dice_values:
                self.dice.append(Die(value))

    def roll(self, indexes=None):
        """
        Rolls the dice in the hand.

        Args:
            indexes (list, optional) : The indexes of the dice to roll. Defaults to None.
        """
        if indexes is None:
            for die in self.dice:
                die.roll()
        else:
            for i in indexes:
                self.dice[i].roll()

    def __str__(self):
        """
        Returns the string representation of the hand.

        Returns:
            str: The string representation of the hand.
        """
        return ", ".join(str(die.get_value()) for die in self.dice)
