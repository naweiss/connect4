from copy import deepcopy
from typing import Tuple
import math

from connect4 import Connect4Game, Player
from evaluation import GreedyEvaluator


class AlphaBetaPlayer:
    """Player for connect4 game which uses the MiniMax algorithm with alpha-beta pruning"""

    def __init__(self, max_depth: int = 4) -> None:
        self.max_depth = max_depth

    @classmethod
    def _minimax(cls, game: Connect4Game, maximizing_player: Player, alpha: float, beta: float, depth: int) -> Tuple[int, float]:
        """Find the best move in a connect4 by using the MiniMax algorithm with alpha-beta pruning

        Args:
            game (Connect4Game): the connect4 game to play the move in
            maximizing_player (Player): the maximizing player
            alpha (float): alpha value for alpha-beta pruning
            beta (float): beta value for alpha-beta pruning
            depth (int): the evaluation depth

        Returns:
            int: best move
            int: score of the best move
        """
        game_over, _ = game.check_win()
        if depth == 0 or game_over:
            return -1, GreedyEvaluator.evaluate(game, maximizing_player)

        if game.current_player == maximizing_player:
            best_column, best_score = -1, -math.inf
        else: # minimizing
            best_column, best_score = -1, math.inf

        for column in range(game.board.shape[1]):
            if not game.is_valid_move(column):
                continue

            future_game = deepcopy(game)
            future_game.play_move(column)
            future_game.switch_turn()
            _, score = cls._minimax(future_game, maximizing_player, alpha, beta, depth - 1)

            if game.current_player == maximizing_player:
                if best_column == -1 or score > best_score:
                    best_column, best_score = column, score
                alpha = max(alpha, best_score)
            else: # minimizing
                if best_column == -1 or score < best_score:
                    best_column, best_score = column, score
                beta = min(beta, best_score)

            if alpha >= beta:
                break

        return best_column, best_score

    def choose_move(self, game: Connect4Game) -> int:
        """Choose a valid move to play in the game

        Args:
            game (Connect4Game): the connect4 game to play the move in

        Returns:
            int: Selected column index.
        """
        move, score = self._minimax(game, game.current_player, -math.inf, math.inf, self.max_depth)
        return move
