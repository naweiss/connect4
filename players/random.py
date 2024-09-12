import numpy as np

from connect4 import Connect4Game


class RandomPlayer:
    """Player for connect4 game which play random moves"""

    def choose_move(self, game: Connect4Game) -> int:
        """Asks the user for a valid move to play.

        Args:
            game (Connect4Game): the connect4 game to play the move in

        Returns:
            int: Selected column index.
        """
        while True:
            column = np.random.randint(game.board.shape[1])
            if game.is_valid_move(column):
                return column
