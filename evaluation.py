from copy import deepcopy
import itertools

import numpy as np

from connect4 import Connect4Game


class GreedyEvaluator:
    LENGTH_TO_SCORE = {
        1: 1,
        2: 2,
        3: 4,
        4: float('inf'),
        5: float('inf'),
        6: float('inf'),
        7: float('inf'),
    }

    @classmethod
    def _evaluate_rows(cls, game: Connect4Game) -> float:
        score = 0
        for row in range(game.board.shape[0]):
            for player, pieces in itertools.groupby(game.board[row, :]):
                if player == game.current_player:
                    score += cls.LENGTH_TO_SCORE[len(list(pieces))]
        return score

    @classmethod
    def _evaluate_columns(cls, game: Connect4Game) -> float:
        score = 0
        for column in range(game.board.shape[1]):
            for player, pieces in itertools.groupby(game.board[:, column]):
                if player == game.current_player:
                    score += cls.LENGTH_TO_SCORE[len(list(pieces))]
        return score

    @classmethod
    def _evaluate_diagonals(cls, game: Connect4Game) -> float:
        score = 0
        for diagonal_offset in range(-game.board.shape[1] + 1, game.board.shape[1]):
            diagonal = np.diagonal(game.board, offset=diagonal_offset)
            second_diagonal = np.diagonal(np.fliplr(game.board), offset=diagonal_offset)

            for player, pieces in itertools.groupby(diagonal):
                if player == game.current_player:
                    score += cls.LENGTH_TO_SCORE[len(list(pieces))]

            for player, pieces in itertools.groupby(second_diagonal):
                if player == game.current_player:
                    score += cls.LENGTH_TO_SCORE[len(list(pieces))]

        return score

    @classmethod
    def other_player_can_win(cls, game: Connect4Game) -> bool:
        for column in range(game.board.shape[1]):
            future_game = deepcopy(game)
            future_game.switch_turn()
            future_game.play_move(column)
            game_over, winner = future_game.check_win()
            if game_over:
                return True
        return False

    @classmethod
    def evaluate(cls, game: Connect4Game) -> float:
        score = cls._evaluate_rows(game) + cls._evaluate_columns(game) + cls._evaluate_diagonals(game)
        if score == float('inf') or game.check_tie():  # game ended
            return score
        if cls.other_player_can_win(game):  # make sure other player can be first
            return float('-inf')
        return score
