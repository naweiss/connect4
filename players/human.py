from connect4 import Connect4Game

import numpy as np


class HumanPlayer:
    def __init__(self, game: Connect4Game) -> None:
        self.game = game

    def choose_move(self) -> int:
        """Asks the user for a valid move to play.

        Returns:
            int: Selected column index.
        """
        print("Enter a number between 0 and 6:", end="")
        column = int(input())
        while True:
            if self.game.is_valid_move(column):
                return column
            print("Invalid column, enter a number between 0 and 6:", end="")
            column = int(input())

