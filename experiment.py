from typing import Tuple, Optional

from connect4 import Connect4Game, Player
from players.greedy import GreedyPlayer
from players.alpha_beta import AlphaBetaPlayer
from players.pvs import PVSPlayer
from players.mcts import MCTSPlayer

EXP_TIMES = 12


def run_one_game(first_player, second_player, starting_player: Player) -> Tuple[Optional[Player], int]:
    game = Connect4Game(starting_player)
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


def run_one_experiment(first_player, second_player, times: int) -> Tuple[int, int]:
    total_moving_steps = 0
    first_player_wins = 0

    for i in range(times):
        # Alternate the starting player
        starting_player = Player.FIRST if i % 2 == 0 else Player.SECOND
        winner, current_moving_steps = run_one_game(first_player, second_player, starting_player)
        total_moving_steps += current_moving_steps
        if winner is Player.FIRST:
            first_player_wins += 1

    return first_player_wins, total_moving_steps


def main() -> None:
    # Greedy VS Alpha Beta Pruning:
    print("Greedy VS Alpha Beta Pruning:")
    wins, steps = run_one_experiment(GreedyPlayer(), AlphaBetaPlayer(), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Greedy VS PVS:
    print("Greedy VS PVS:")
    wins, steps = run_one_experiment(GreedyPlayer(), PVSPlayer(), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Greedy VS MCTS:
    print("Greedy VS MCTS:")
    wins, steps = run_one_experiment(GreedyPlayer(), MCTSPlayer(), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Alpha Beta Pruning VS Greedy:
    print("Alpha Beta Pruning VS Greedy:")
    wins, steps = run_one_experiment(AlphaBetaPlayer(), GreedyPlayer(), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Alpha Beta Pruning VS PVS:
    print("Alpha Beta Pruning VS PVS:")
    wins, steps = run_one_experiment(AlphaBetaPlayer(), PVSPlayer(), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Alpha Beta Pruning VS MCTS:
    print("Alpha Beta Pruning VS MCTS:")
    wins, steps = run_one_experiment(AlphaBetaPlayer(), MCTSPlayer(), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # PVS VS Greedy:
    print("PVS VS Greedy:")
    wins, steps = run_one_experiment(PVSPlayer(), GreedyPlayer(), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # PVS VS Alpha Beta Pruning:
    print("PVS VS Alpha Beta Pruning:")
    wins, steps = run_one_experiment(PVSPlayer(), AlphaBetaPlayer(), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # PVS VS MCTS:
    print("PVS VS MCTS:")
    wins, steps = run_one_experiment(PVSPlayer(), MCTSPlayer(), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # MCTS VS Greedy:
    print("MCTS VS Greedy:")
    wins, steps = run_one_experiment(MCTSPlayer(), GreedyPlayer(), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # MCTS VS Alpha Beta Pruning:
    print("MCTS VS Alpha Beta Pruning:")
    wins, steps = run_one_experiment(MCTSPlayer(), AlphaBetaPlayer(), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # MCTS VS PVS:
    print("MCTS VS PVS:")
    wins, steps = run_one_experiment(MCTSPlayer(), PVSPlayer(), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()


if __name__ == "__main__":
    main()
