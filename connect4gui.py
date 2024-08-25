import sys
import os

from connect4 import Connect4Game, Player


class Connect4Ui:
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
        print("Player {} turn [{}]".format(self.game.current_player, 'X' if self.game.current_player == Player.FIRST else 'O'))
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

    def get_player_move(self) -> int:
        """Asks the user for a valid move to play.

        Returns:
            int: Selected column index.
        """
        print("Enter a number between 0 and 6:", end="")
        column = int(input())
        while True:
            if self.game.is_valid_move(column):
                return column
            print("Invalid column, enter a number between 0 and 6:", end="")
            column = int(input())

    def show_winner(self, winner: Player) -> None:
        if winner is None:
            print("\n\nTIE!!!")
        else:
            print("\n\nPLAYER {} [{}] WON!!!".format(winner, 'X' if winner == Player.FIRST else 'O'))


def main():
    game = Connect4Game()
    ui = Connect4Ui(game)

    # Game loop
    while True:
        ui.show()

        # Check game over
        game_over, winner = game.check_win()
        if game_over is True:
            ui.show_winner(winner)
            break

        column = ui.get_player_move()
        game.play_move(column)
        game.switch_turn()

if __name__ == "__main__":
    main()

