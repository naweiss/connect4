import numpy as np

from connect4 import Connect4Game, Player
from connect4gui import Connect4Ui
from players.greedy import GreedyPlayer
from players.alpha_beta import AlphaBetaPlayer


def main() -> None:
    game = Connect4Game(starting_player=Player.FIRST)
    game.play_move(2)
    game.switch_turn()
    ui = Connect4Ui(game)
    players = [GreedyPlayer(), AlphaBetaPlayer(max_depth=4)]

    # Game loop
    while True:
        ui.show()

        # Check game over
        game_over, winner = game.check_win()
        if game_over is True:
            ui.show_winner(winner)
            break

        current_player = players[0] if game.current_player == Player.FIRST else players[1]
        column = current_player.choose_move(game)
        game.play_move(column)
        # import time; time.sleep(1)
        game.switch_turn()


if __name__ == "__main__":
    main()
