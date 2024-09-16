from copy import deepcopy

from connect4 import Connect4Game
from evaluation import GreedyEvaluator

DEPTH = 4


def get_valid_locations(game: Connect4Game):
    result = []
    for i in range(game.board.shape[1]):
        if game.is_valid_move(i):
            result.append(i)
    return result


class AlphaBetaPlayer:
    """Player for connect4 game which uses the AlphaBeta algorithm"""

    @staticmethod
    def minimax(game: Connect4Game, depth, alpha, beta, maximizing_player) -> (int, float):
        is_win, winner = game.check_win()
        if is_win:
            if winner is maximizing_player:
                return -1, float('inf')
            elif winner is None:
                return -1, 0
            else:  # Game is over, no more valid moves
                return -1, float('-inf')
        elif depth == 0:
            return -1, GreedyEvaluator.evaluate(game)

        valid_locations = get_valid_locations(game)

        if maximizing_player:
            value = float('-inf')
            column = -1
            for col in valid_locations:
                future_game = deepcopy(game)
                future_game.play_move(column)
                new_score = AlphaBetaPlayer.minimax(future_game, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:  # Minimizing player
            value = float('inf')
            column = -1
            for col in valid_locations:
                future_game = deepcopy(game)
                future_game.play_move(column)
                new_score = AlphaBetaPlayer.minimax(future_game, depth - 1, alpha, beta, True)[1]
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
        return self.minimax(game, DEPTH, float('-inf'), float('-inf'), True)[0]
