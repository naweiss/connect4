from connect4 import Connect4Game

import numpy as np


class HumanPlayer:
    def __init__(self, game: Connect4Game) -> None:
        self.game = game

    def prompt_for_move(self) -> int:
        """Asks the user for a move to play.

        Returns:
            int: Selected column index.
        """
        while True:
            print("Enter a number between 0 and 6:", end="")
            try:
                return int(input())
            except ValueError:
                pass

    def choose_move(self) -> int:
        """Asks the user for a valid move to play.

        Returns:
            int: Selected column index.
        """
        while True:
            column = self.prompt_for_move()
            if self.game.is_valid_move(column):
                return column
