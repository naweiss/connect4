from __future__ import annotations
from copy import deepcopy
from typing import Dict, Optional, Tuple
import math
import random

from connect4 import Connect4Game, Player


class Node:
    """Node in the Monte Carlo Tree"""

    def __init__(self, game: Connect4Game, parent: Optional[Node] = None) -> None:
        self.wins = 0
        self.games_played = 0
        self.root_game = game
        self.parent = parent
        self.valid_moves = game.get_valid_moves()
        self.sub_games: Dict[int, Node] = {}

    def expand(self) -> Optional[Node]:
        for column in self.valid_moves:
            if column not in self.sub_games:
                self.sub_games[column] = self.create_child(column)
                return self.sub_games[column]
        return self

    def create_child(self, column: int) -> Node:
        future_game = deepcopy(self.root_game)
        future_game.play_move(column)
        future_game.switch_turn()
        return Node(future_game, self)

    def is_leaf(self) -> bool:
        all_children_expended = list(self.sub_games.keys()) == self.valid_moves and len(self.valid_moves) > 0
        return self.games_played == 0 or not all_children_expended

    def calculate_uct(self) -> float:
        return (self.wins / self.games_played) + 2 * math.sqrt(math.log(self.parent.games_played) / self.games_played)

    def select_child(self) -> Node:
        sub_games_utc = {sub_game: sub_game.calculate_uct()
                         for sub_game in self.sub_games.values()}
        return max(sub_games_utc, key=sub_games_utc.get)


class MCTSPlayer:
    """Player for connect4 game which uses the Monte Carlo Tree Search algorithm"""

    def __init__(self, iterations: int = 300) -> None:
        self.iterations = iterations

    @staticmethod
    def simulation(game: Connect4Game) -> Player:
        """Perform a random game simulation.

        Args:
            game (Connect4Game): the connect4 game to play the move in

        Returns:
            Player: The winner of the game if any
        """
        future_game = deepcopy(game)
        while not future_game.check_win()[0]:
            future_game.play_move(random.choice(future_game.get_valid_moves()))
            future_game.switch_turn()
        return future_game.check_win()[1]

    @staticmethod
    def selection(root: Node) -> Node:
        node = root
        while not node.is_leaf():
            node = node.select_child()
        return node

    @staticmethod
    def backpropagation(leaf: Node, winner: Player) -> None:
        node = leaf
        while node is not None:
            if winner != node.root_game.current_player:
                node.wins += 1
            node.games_played += 1
            node = node.parent

    @staticmethod
    def expansion(leaf: Node) -> Optional[Node]:
        return leaf.expand()

    def choose_move(self, game: Connect4Game) -> Tuple[int, int]:
        """Choose a valid move to play in the game

        Args:
            game (Connect4Game): the connect4 game to play the move in

        Returns:
            int: Selected column index.
            int: steps.
        """
        root = Node(game)
        for i in range(self.iterations):
            leaf = self.selection(root)
            if leaf is None:
                break

            child = self.expansion(leaf)

            winner = self.simulation(child.root_game)

            self.backpropagation(child, winner)

        # return the moves with the highest win rate
        return max(root.sub_games, key=lambda column: root.sub_games.get(column).games_played), 1
