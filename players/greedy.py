from connect4 import Connect4Game
from evaluation import GreedyEvaluator


class GreedyPlayer:
    def __init__(self, game: Connect4Game) -> None:
        self.evaluator = GreedyEvaluator(game)
        self.game = game

    def choose_move(self) -> int:
        best_column, best_score = -1, float('-inf')
        for column in range(self.game.board.shape[1]):
            score = self.evaluator.evaluate(column)
            if score >= best_score and self.game.is_valid_move(column):
                best_column, best_score = column, score
        return best_column
