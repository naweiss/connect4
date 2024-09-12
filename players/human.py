from connect4 import Connect4Game


class HumanPlayer:
    """Human player for connect4 game"""

    @staticmethod
    def _prompt_for_move() -> int:
        """Asks the user for a move to play.

        Returns:
            int: Selected column index.
        """
        while True:
            print("Enter a number between 0 and 6:", end="")
            try:
                return int(input())
            except ValueError:
                pass

    def choose_move(self, game: Connect4Game) -> int:
        """Asks the user for a valid move to play.

        Args:
            game (Connect4Game): the connect4 game to play the move in

        Returns:
            int: Selected column index.
        """
        while True:
            column = self._prompt_for_move()
            if game.is_valid_move(column):
                return column
