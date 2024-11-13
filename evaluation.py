from copy import deepcopy
import itertools
import math

import numpy as np

from connect4 import Connect4Game, Player


class GreedyEvaluator:
    """Evaluate a game of connect4"""

    LENGTH_TO_SCORE = {
        1: 1.0,
        2: 2.0,
        3: 4.0,
        4: math.inf,
        5: math.inf,
        6: math.inf,
        7: math.inf,
    }

    @classmethod
    def _evaluate_rows(cls, game: Connect4Game, evaluated_player: Player) -> float:
        score = 0.0
        for row in range(Connect4Game.BOARD_SIZE[0]):
            for player, pieces in itertools.groupby(game.board[row, :]):
                if player == evaluated_player:
                    score += cls.LENGTH_TO_SCORE[len(list(pieces))]
                    if score == math.inf:
                        return score
        return score

    @classmethod
    def _evaluate_columns(cls, game: Connect4Game, evaluated_player: Player) -> float:
        score = 0.0
        for column in range(Connect4Game.BOARD_SIZE[1]):
            for player, pieces in itertools.groupby(game.board[:, column]):
                if player == evaluated_player:
                    score += cls.LENGTH_TO_SCORE[len(list(pieces))]
                    if score == math.inf:
                        return score
        return score

    @classmethod
    def _evaluate_diagonals(cls, game: Connect4Game, evaluated_player: Player) -> float:
        score = 0.0
        for diagonal_offset in range(-Connect4Game.BOARD_SIZE[1] + 1, Connect4Game.BOARD_SIZE[1]):
            diagonal = np.diagonal(game.board, offset=diagonal_offset)
            for player, pieces in itertools.groupby(diagonal):
                if player == evaluated_player:
                    score += cls.LENGTH_TO_SCORE[len(list(pieces))]
                    if score == math.inf:
                        return score

            second_diagonal = np.diagonal(np.fliplr(game.board), offset=diagonal_offset)
            for player, pieces in itertools.groupby(second_diagonal):
                if player == evaluated_player:
                    score += cls.LENGTH_TO_SCORE[len(list(pieces))]
                    if score == math.inf:
                        return score

        return score

    """
    @classmethod
    def _other_player_can_win(cls, game: Connect4Game, player: Player) -> bool:
        for column in range(Connect4Game.BOARD_SIZE[1]):
            future_game = deepcopy(game)
            future_game.play_move(column)
            game_over, winner = future_game.check_win()
            if game_over and winner != player:
                return True
        return False
    """

    @classmethod
    def evaluate(cls, game: Connect4Game, player: Player) -> float:
        rows_score = cls._evaluate_rows(game, player)
        if rows_score == math.inf:
            return math.inf

        columns_score = cls._evaluate_rows(game, player)
        if columns_score == math.inf:
            return math.inf

        diagonals_score = cls._evaluate_diagonals(game, player)
        if diagonals_score == math.inf:
            return math.inf

        opponent = Player.SECOND if player == Player.FIRST else Player.FIRST

        opponent_rows_score = cls._evaluate_rows(game, opponent)
        if opponent_rows_score == math.inf:
            return -math.inf

        opponent_columns_score = cls._evaluate_rows(game, opponent)
        if opponent_columns_score == math.inf:
            return -math.inf

        opponent_diagonals_score = cls._evaluate_diagonals(game, opponent)
        if opponent_diagonals_score == math.inf:
            return -math.inf

        player_score = rows_score + columns_score + diagonals_score
        opponent_score = opponent_rows_score + opponent_columns_score + opponent_diagonals_score
        total_score = player_score - opponent_score

        return total_score
