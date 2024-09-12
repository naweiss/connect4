from copy import deepcopy

from connect4 import Connect4Game
from evaluation import GreedyEvaluator


class AlphaBetaPlayer:
    """Player for connect4 game which uses the AlphaBeta algorithm"""

    @staticmethod
    def _evaluate_move(game: Connect4Game, column: int) -> float:
        """Evaluate a connect4 move in a specific game.

        Args:
            game (Connect4Game): the connect4 game to play the move in
            column (int): the column to play the move in

        Returns:
            int: evaluated score for the given move
        """
        future_game = deepcopy(game)
        future_game.play_move(column)
        return GreedyEvaluator.evaluate(future_game)

    def choose_move(self, game: Connect4Game) -> int:
        """Asks the user for a valid move to play.

        Args:
            game (Connect4Game): the connect4 game to play the move in

        Returns:
            int: Selected column index.
        """
        best_column, best_score = -1, float('-inf')
        for column in range(game.board.shape[1]):
            if game.is_valid_move(column):
                score = self._evaluate_move(game, column)
                if score >= best_score and game.is_valid_move(column):
                    best_column, best_score = column, score
        return best_column
