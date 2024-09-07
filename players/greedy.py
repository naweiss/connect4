from copy import deepcopy

from connect4 import Connect4Game
from evaluation import GreedyEvaluator

class GreedyPlayer:
    def __init__(self, game: Connect4Game) -> None:
        self.game = game

    def choose_move(self) -> int:
        best_column, best_score = -1, float('-inf')
        for column in range(self.game.board.shape[1]):
            future_game = deepcopy(self.game)
            future_game.play_move(column)
            score = GreedyEvaluator.evaluate(future_game)
            if score >= best_score and self.game.is_valid_move(column):
                best_column, best_score = column, score
        return best_column
