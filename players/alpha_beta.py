from copy import deepcopy

from connect4 import Connect4Game
from evaluation import GreedyEvaluator

DEPTH = 4


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

    @staticmethod
    def minimax(game: Connect4Game, depth, alpha, beta, maximizing_player):
        # TODO: implement get_valid_locations()
        valid_locations = game.get_valid_locations()
        is_win, winner = game.check_win()
        if is_win:
            if winner is maximizing_player:
                return None, float('inf')
            elif winner is None:
                return None, 0
            else:  # Game is over, no more valid moves
                return None, float('-inf')
        elif depth == 0:
            return None, GreedyEvaluator.evaluate(game)

        if maximizing_player:
            # TODO: FIX
            value = float('-inf')
            column = -1
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, AI_PIECE)
                new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:  # Minimizing player
            # TODO: FIX
            value = float('inf')
            column = -1
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, PLAYER_PIECE)
                new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

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
