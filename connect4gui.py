import sys
import os

from connect4 import Connect4Game, Player


class Connect4Ui:
    PLAYER_TO_SYMBOL = {
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
        print("Player {} turn [{}]".format(self.game.current_player, self.PLAYER_TO_SYMBOL[self.game.current_player]))
        print("+---------------------------+")
        for row in range(self.game.board.shape[0]):
            for column in range(self.game.board.shape[1]):
                if self.game.board[row, column] == Player.FIRST:
                    print("| X", end=" ")
                elif self.game.board[row, column] == Player.SECOND:
                    print("| O", end=" ")
                else:
                    print("|  ", end=" ")
            print("|")
        print("+---------------------------+")
        print("| 0   1   2   3   4   5   6 |")
        print("+---------------------------+")

    def show_winner(self, winner: Player) -> None:
        if winner is None:
            print("\n\nTIE!!!")
        else:
            print("\n\nPLAYER {} [{}] WON!!!".format(winner, self.PLAYER_TO_SYMBOL[winner]))

