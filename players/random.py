from connect4 import Connect4Game

import numpy as np


class RandomPlayer:
    def __init__(self, game: Connect4Game) -> None:
        self.game = game

    def choose_move(self) -> int:
        column = np.random.randint(self.game.board.shape[1])
        return column
