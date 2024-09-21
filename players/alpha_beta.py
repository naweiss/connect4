from copy import deepcopy

from connect4 import Connect4Game
from evaluation import GreedyEvaluator

DEPTH = 4


def get_valid_locations(game: Connect4Game):
    result = []
    for i in range(Connect4Game.BOARD_SIZE[1]):
        if game.is_valid_move(i):
            result.append(i)
    return result


class AlphaBetaPlayer:
    """Player for connect4 game which uses the AlphaBeta algorithm"""

    @staticmethod
    def minimax(game: Connect4Game, eval_player, depth, alpha, beta, maximizing_player=True) -> (int, float):
        game_over, winner = game.check_win()
        if game_over:
            if winner is eval_player:
                return -1, float('inf')
            elif winner is None:
                return -1, 0
            else:
                return -1, float('-inf')
        elif depth == 0:
            return -1, GreedyEvaluator.evaluate(game)

        valid_locations = get_valid_locations(game)

        if maximizing_player:
            value = float('-inf')
            best_col = -1
            for col in valid_locations:
                future_game = deepcopy(game)
                future_game.play_move(col)
                new_score = AlphaBetaPlayer.minimax(future_game, eval_player, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    best_col = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return best_col, value

        else:  # Minimizing player
            value = float('inf')
            best_col = -1
            for col in valid_locations:
                future_game = deepcopy(game)
                future_game.play_move(col)
                new_score = AlphaBetaPlayer.minimax(future_game, eval_player, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    best_col = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return best_col, value

    def choose_move(self, game: Connect4Game) -> int:
        """Asks the user for a valid move to play.

        Args:
            game (Connect4Game): the connect4 game to play the move in

        Returns:
            int: Selected column index.
        """
        return self.minimax(game, game.current_player, DEPTH, float('-inf'), float('inf'))[0]
