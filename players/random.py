import numpy as np

from connect4 import Connect4Game


class RandomPlayer:
    """Player for connect4 game which play random moves"""

    def choose_move(self, game: Connect4Game) -> int:
        """Choose a valid move to play in the game

        Args:
            game (Connect4Game): the connect4 game to play the move in

        Returns:
            int: Selected column index.
        """
        while True:
            column = np.random.randint(Connect4Game.BOARD_SIZE[1])
            if game.is_valid_move(column):
                return column
