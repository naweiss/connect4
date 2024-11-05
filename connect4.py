"""Based on https://github.com/Gualor/connect4-montecarlo/blob/master/scripts/connect4_mcts.py"""

from typing import Tuple
from enum import IntEnum, auto

import numpy as np


class Player(IntEnum):
    NONE = auto()
    FIRST = auto()
    SECOND = auto()


class Connect4Game:
    """Connect4 game board"""

    BOARD_SIZE = (5, 6)

    def __init__(self, starting_player: Player) -> None:
        self.current_player: Player = starting_player
        self.board: np.ndarray = np.full(shape=self.BOARD_SIZE, fill_value=Player.NONE)

    def is_valid_move(self, column: int) -> bool:
        """Check if a move can be applied to the board.

        Args:
            column (int): Selected column index (starts from 0).

        Returns:
            bool: Move can be applied successfully.
        """
        if column < 0 or column > self.board.shape[1] - 1:
            return False

        return self.board[0, column] == Player.NONE

    def play_move(self, column: int) -> bool:
        """Apply move to board.

        Args:
            column (int): Selected column index (starts from 0).

        Returns:
            bool: Move applied successfully.
        """
        for row in reversed(range(self.board.shape[0])):
            if self.board[row, column] == Player.NONE:
                self.board[row, column] = self.current_player
                return True
        return False

    def switch_turn(self) -> None:
        """Switch turn between players."""
        if self.current_player == Player.FIRST:
            self.current_player = Player.SECOND
        else:
            self.current_player = Player.FIRST

    def check_win(self) -> Tuple[bool, Player]:
        """Check whether the match is over.

        Returns:
            Tuple[bool, Player | None]: Game has ended, winner or None.
        """
        winner = self._check_rows()
        if winner != Player.NONE:
            return True, winner

        winner = self._check_cols()
        if winner != Player.NONE:
            return True, winner

        winner = self._check_diag()
        if winner != Player.NONE:
            return True, winner

        if self.check_tie():
            return True, Player.NONE

        return False, Player.NONE

    @staticmethod
    def _all_identical(array: np.ndarray) -> bool:
        """Checks if all elements in an array are the same.

        Args:
            array (np.ndarray): Array of elements.

        Returns:
            bool: All elements are the same.
        """
        first_value = array[0]
        if first_value == Player.NONE:
            return False
        return np.all(array == first_value)

    def _check_rows(self) -> Player:
        """Check for winner in rows.

        Returns:
            Player | None: Winner or None.
        """
        for row in range(self.board.shape[0]):
            for column in range(self.board.shape[1] - 3):
                if self._all_identical(self.board[row, column: column + 4]):
                    return Player(self.board[row, column])
        return Player.NONE

    def _check_cols(self) -> Player:
        """Check for winner in columns.

        Returns:
            Player | None: Winner or None.
        """
        for column in range(self.board.shape[1]):
            for row in range(self.board.shape[0] - 3):
                if self._all_identical(self.board[row: row + 4, column]):
                    return Player(self.board[row, column])
        return Player.NONE

    def _check_diag(self) -> Player:
        """Check for winner in diagonals.

        Returns:
            Player | None: Winner or None.
        """
        for diagonal_offset in range(-self.board.shape[1] + 1, self.board.shape[1]):
            diagonal = np.diagonal(self.board, offset=diagonal_offset)
            for index in range(diagonal.size - 3):
                if self._all_identical(diagonal[index : index + 4]):
                    return Player(diagonal[index])

            second_diagonal = np.diagonal(np.fliplr(self.board), offset=diagonal_offset)
            for index in range(second_diagonal.size - 3):
                if self._all_identical(second_diagonal[index : index + 4]):
                    return Player(second_diagonal[index])
        return Player.NONE

    def check_tie(self) -> bool:
        """Check if the game is a tie.

        Returns:
            bool: Game is a tie.
        """
        return np.count_nonzero(self.board != Player.NONE) == self.board.size
