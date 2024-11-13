from copy import deepcopy
from typing import Tuple
import math

from connect4 import Connect4Game, Player
from evaluation import GreedyEvaluator


class PVSPlayer:
    """Player for connect4 game which uses the Principal Variation Search algorithm"""

    def __init__(self, max_depth: int = 4) -> None:
        self.max_depth = max_depth

    @classmethod
    def _pvs(cls, game: Connect4Game, maximizing_player: Player, alpha: float, beta: float, depth: int) -> Tuple[
        int, float]:
        """Find the best move in a connect4 by using the MiniMax algorithm,
           with alpha-beta pruning and Principal Variation Search optimization

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
            score = GreedyEvaluator.evaluate(game, maximizing_player)
            return -1, score if game.current_player == maximizing_player else -score

        best_column, best_score = -1, -math.inf

        for column in range(Connect4Game.BOARD_SIZE[1]):
            if not game.is_valid_move(column):
                continue

            future_game = deepcopy(game)
            future_game.play_move(column)
            future_game.switch_turn()

            if best_column == -1 or depth == 1 or (beta - alpha) == 1:
                score = -cls._pvs(future_game, maximizing_player, -beta, -alpha, depth - 1)[1]
            else:
                score = -cls._pvs(future_game, maximizing_player, -alpha - 1, -alpha, depth - 1)[1]
                if score > alpha and beta - alpha > 1:
                    score = -cls._pvs(future_game, maximizing_player, -beta, -alpha, depth - 1)[1]

            if best_column == -1 or score > best_score:
                best_column, best_score = column, score
            alpha = max(alpha, score)

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
        move, score = self._pvs(game, game.current_player, -math.inf, math.inf, self.max_depth)
        return move
