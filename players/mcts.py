from copy import deepcopy

from connect4 import Connect4Game
from evaluation import Evaluator


class MCTSPlayer:
    """Player for connect4 game which uses the Monte Carlo Tree Search algorithm"""

    def __init__(self, evaluator: type[Evaluator]) -> None:
        self.evaluator = evaluator

    def _evaluate_move(self, game: Connect4Game, column: int) -> float:
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
        return self.evaluator.evaluate(future_game, game.current_player)

    def choose_move(self, game: Connect4Game) -> int:
        """Choose a valid move to play in the game

        Args:
            game (Connect4Game): the connect4 game to play the move in

        Returns:
            int: Selected column index.
        """
        best_column, best_score = 0, float('-inf')
        for column in game.get_valid_moves():

            score = self._evaluate_move(game, column)
            if score >= best_score:
                best_column, best_score = column, score
        return best_column
