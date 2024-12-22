import random
from typing import Tuple

from connect4 import Connect4Game


class RandomPlayer:
    """Player for connect4 game which play random moves"""

    def choose_move(self, game: Connect4Game) -> Tuple[int, int]:
        """Choose a valid move to play in the game

        Args:
            game (Connect4Game): the connect4 game to play the move in

        Returns:
            int: Selected column index.
        """
        return random.choice(game.get_valid_moves()), 1
