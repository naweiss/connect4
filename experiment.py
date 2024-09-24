from typing import Tuple

from connect4 import Connect4Game, Player
from players.greedy import GreedyPlayer
from players.alpha_beta import AlphaBetaPlayer
from players.pvs import PVSPlayer
from players.mcts import MCTSPlayer


def run_one_game(game: Connect4Game, first_player, second_player) -> Tuple[Player, int]:
    moving_steps = 0

    # Game loop
    while True:
        current_player = first_player if game.current_player == Player.FIRST else second_player
        column = current_player.choose_move(game)
        game.play_move(column)
        moving_steps += 1
        game.switch_turn()

        # Check game over
        game_over, winner = game.check_win()
        if game_over:
            return winner, moving_steps


def run_one_experiment(first_player, second_player) -> Tuple[int, int]:
    total_moving_steps = 0
    first_player_wins = 0

    for starting_player in [Player.FIRST, Player.SECOND]:
        for column in range(Connect4Game.BOARD_SIZE[1]):
            game = Connect4Game(starting_player)
            game.play_move(column)
            game.switch_turn()

            winner, current_moving_steps = run_one_game(game, first_player, second_player)
            total_moving_steps += current_moving_steps
            if winner is Player.FIRST:
                first_player_wins += 1

    return first_player_wins, total_moving_steps


def main() -> None:
    # Greedy VS Alpha Beta Pruning:
    print("Greedy VS Alpha Beta Pruning:")
    wins, steps = run_one_experiment(GreedyPlayer(), AlphaBetaPlayer())
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Greedy VS PVS:
    print("Greedy VS PVS:")
    wins, steps = run_one_experiment(GreedyPlayer(), PVSPlayer())
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Greedy VS MCTS:
    print("Greedy VS MCTS:")
    wins, steps = run_one_experiment(GreedyPlayer(), MCTSPlayer())
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Alpha Beta Pruning VS Greedy:
    print("Alpha Beta Pruning VS Greedy:")
    wins, steps = run_one_experiment(AlphaBetaPlayer(), GreedyPlayer())
    print("Alpha Beta Pruning wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Alpha Beta Pruning VS PVS:
    print("Alpha Beta Pruning VS PVS:")
    wins, steps = run_one_experiment(AlphaBetaPlayer(), PVSPlayer())
    print("Alpha Beta Pruning wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Alpha Beta Pruning VS MCTS:
    print("Alpha Beta Pruning VS MCTS:")
    wins, steps = run_one_experiment(AlphaBetaPlayer(), MCTSPlayer())
    print("Alpha Beta Pruning wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # PVS VS Greedy:
    print("PVS VS Greedy:")
    wins, steps = run_one_experiment(PVSPlayer(), GreedyPlayer())
    print("PVS wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # PVS VS Alpha Beta Pruning:
    print("PVS VS Alpha Beta Pruning:")
    wins, steps = run_one_experiment(PVSPlayer(), AlphaBetaPlayer())
    print("PVS wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # PVS VS MCTS:
    print("PVS VS MCTS:")
    wins, steps = run_one_experiment(PVSPlayer(), MCTSPlayer())
    print("PVS wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # MCTS VS Greedy:
    print("MCTS VS Greedy:")
    wins, steps = run_one_experiment(MCTSPlayer(), GreedyPlayer())
    print("MCTS wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # MCTS VS Alpha Beta Pruning:
    print("MCTS VS Alpha Beta Pruning:")
    wins, steps = run_one_experiment(MCTSPlayer(), AlphaBetaPlayer())
    print("MCTS wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # MCTS VS PVS:
    print("MCTS VS PVS:")
    wins, steps = run_one_experiment(MCTSPlayer(), PVSPlayer())
    print("MCTS wins: ", wins)
    print("Moving steps: ", steps)
    print()


if __name__ == "__main__":
    main()
