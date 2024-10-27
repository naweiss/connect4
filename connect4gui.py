import sys
import os

from connect4 import Connect4Game, Player


class Connect4Ui:
    """Console base UI for connect4 game"""

    PLAYER_TO_SYMBOL = {
        Player.NONE: ' ',
        Player.FIRST: 'X',
        Player.SECOND: 'O',
    }

    def __init__(self, game: Connect4Game) -> None:
        self.game = game

    def _clear_screen(self) -> None:
        """Clears the console."""
        if sys.platform == 'linux':
            os.system('clear')
        elif sys.platform == 'win32':
            os.system('cls')
        else:
            raise NotImplementedError()

    def show(self) -> None:
        """Print out game board on console."""
        self._clear_screen()
        print("{} player turn [{}]".format(self.game.current_player.name.lower(), self.PLAYER_TO_SYMBOL[self.game.current_player]))
        print("+" + "-" * (4 * Connect4Game.BOARD_SIZE[1] - 1) + "+")
        for row in range(Connect4Game.BOARD_SIZE[0]):
            for column in range(Connect4Game.BOARD_SIZE[1]):
                print("| {} ".format(self.PLAYER_TO_SYMBOL[self.game.board[row, column]]), end="")
            print("|")
        print("+" + "-" * (4 * Connect4Game.BOARD_SIZE[1] - 1) + "+")
        for column in range(Connect4Game.BOARD_SIZE[1]):
            print("| {} ".format(column), end="")
        print("|")
        print("+" + "-" * (4 * Connect4Game.BOARD_SIZE[1] - 1) + "+")

    def show_winner(self, winner: Player) -> None:
        """Print the winner of the game"""
        print("\n")
        if winner is Player.NONE:
            print("TIE!!!")
        else:
            print("{} player [{}] WON!!!".format(winner.name.lower(), self.PLAYER_TO_SYMBOL[winner]))

