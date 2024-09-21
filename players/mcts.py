from copy import deepcopy

from connect4 import Connect4Game
from evaluation import GreedyEvaluator


class MCTSPlayer:
    """Player for connect4 game which uses the Monte Carlo Tree Search algorithm"""

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
        future_game.switch_turn()
        return GreedyEvaluator.evaluate(future_game, game.current_player)

    def choose_move(self, game: Connect4Game) -> int:
        """Choose a valid move to play in the game

        Args:
            game (Connect4Game): the connect4 game to play the move in

        Returns:
            int: Selected column index.
        """
        best_column, best_score = -1, float('-inf')
        for column in range(Connect4Game.BOARD_SIZE[1]):
            if game.is_valid_move(column):
                score = self._evaluate_move(game, column)
                if score >= best_score and game.is_valid_move(column):
                    best_column, best_score = column, score
        return best_column
