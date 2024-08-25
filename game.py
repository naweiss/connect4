from connect4 import Connect4Game, Player
from connect4gui import Connect4Ui
from players.human import HumanPlayer
from players.greedy import GreedyPlayer
from players.random import RandomPlayer


def main():
    game = Connect4Game()
    ui = Connect4Ui(game)
    players = [GreedyPlayer(game), RandomPlayer(game)]

    # Game loop
    while True:
        ui.show()

        # Check game over
        game_over, winner = game.check_win()
        if game_over is True:
            ui.show_winner(winner)
            break

        current_player = players[0] if game.current_player == Player.FIRST else players[1]
        column = current_player.choose_move()
        game.play_move(column)
        game.switch_turn()

if __name__ == "__main__":
    main()
