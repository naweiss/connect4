import numpy as np

from connect4 import Connect4Game


class RandomPlayer:
    def __init__(self, game: Connect4Game) -> None:
        self.game = game

    def choose_move(self) -> int:
        while True:
            column = np.random.randint(self.game.board.shape[1])
            if self.game.is_valid_move(column):
                return column
