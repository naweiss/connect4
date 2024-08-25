from copy import deepcopy
import itertools

import numpy as np

from connect4 import Connect4Game, Player


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

    def __init__(self, game: Connect4Game) -> None:
        self.game = game

    @classmethod
    def _evaluate_rows(cls, future_game: Connect4Game) -> float:
        score = 0
        for row in range(future_game.board.shape[0]):
            for player, pieces in itertools.groupby(future_game.board[row, :]):
                if player == future_game.current_player:
                    score += cls.LENGTH_TO_SCORE[len(list(pieces))]
        return score

    @classmethod
    def _evaluate_columns(cls, future_game: Connect4Game) -> float:
        score = 0
        for column in range(future_game.board.shape[1]):
            for player, pieces in itertools.groupby(future_game.board[:, column]):
                if player == future_game.current_player:
                    score += cls.LENGTH_TO_SCORE[len(list(pieces))]
        return score

    @classmethod
    def _evaluate_diagonals(cls, future_game: Connect4Game) -> float:
        score = 0
        for diagonal_offset in range(-future_game.board.shape[1] + 1, future_game.board.shape[1]):
            diagonal = np.diagonal(future_game.board, offset=diagonal_offset)
            second_diagonal = np.diagonal(np.fliplr(future_game.board), offset=diagonal_offset)

            for player, pieces in itertools.groupby(diagonal):
                if player == future_game.current_player:
                    score += cls.LENGTH_TO_SCORE[len(list(pieces))]

            for player, pieces in itertools.groupby(second_diagonal):
                if player == future_game.current_player:
                    score += cls.LENGTH_TO_SCORE[len(list(pieces))]

        return score

    @classmethod
    def other_player_can_win(cls, future_game: Connect4Game) -> bool:
        for column in range(future_game.board.shape[1]):
            next_future_game = deepcopy(future_game)
            next_future_game.switch_turn()
            next_future_game.play_move(column)
            game_over, winner = next_future_game.check_win()
            if game_over:
                return True
        return False

    def evaluate(self, column: int) -> float:
        future_game = deepcopy(self.game)
        future_game.play_move(column)

        score = self._evaluate_rows(future_game) + self._evaluate_columns(future_game) + self._evaluate_diagonals(future_game)
        if score != float('inf'):
            if self.other_player_can_win(future_game):
                return float('-inf')
        return score
