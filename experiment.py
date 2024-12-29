from typing import Tuple

from connect4 import Connect4Game, Player
from evaluation import Evaluator, GreedyEvaluator  # , ExternalEvaluator
from players.greedy import GreedyPlayer
from players.alpha_beta import AlphaBetaPlayer
from players.pvs import PVSPlayer
from players.mcts import MCTSPlayer
from print_helpers import table_print, table_header_print


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
        for starting_column in range(Connect4Game.BOARD_SIZE[1]):
            game = Connect4Game(starting_player)
            game.play_move(starting_column)
            game.switch_turn()

            winner, current_moving_steps = run_one_game(game, first_player, second_player)
            total_moving_steps += current_moving_steps
            if winner == Player.FIRST:
                first_player_wins += 1

    return first_player_wins, total_moving_steps


def experiment_header_print(algorithm_name: str):
    print("Experiment results of", algorithm_name)
    table_header_print(["Opponent name", "Win times", "Moving steps"])


def experiment(evaluator: type[Evaluator]) -> None:
    experiment_header_print("Greedy")
    # Greedy VS Alpha Beta Pruning:
    wins, steps = run_one_experiment(GreedyPlayer(evaluator), AlphaBetaPlayer(evaluator))
    t_wins, t_steps = wins, steps
    table_print(["Alpha-beta pruning", wins, steps])
    # Greedy VS MCTS:
    wins, steps = run_one_experiment(GreedyPlayer(evaluator), MCTSPlayer())
    t_wins += wins
    t_steps += steps
    table_print(["Monte Carlo", wins, steps])
    # Greedy VS PVS:
    wins, steps = run_one_experiment(GreedyPlayer(evaluator), PVSPlayer(evaluator))
    t_wins += wins
    t_steps += steps
    table_print(["PVS", wins, steps])
    table_print(["Total", t_wins, t_steps])
    print()

    experiment_header_print("Alpha-beta pruning")
    # Alpha Beta Pruning VS Greedy:
    wins, steps = run_one_experiment(AlphaBetaPlayer(evaluator), GreedyPlayer(evaluator))
    t_wins, t_steps = wins, steps
    table_print(["Greedy", wins, steps])
    # Alpha Beta Pruning VS MCTS:
    wins, steps = run_one_experiment(AlphaBetaPlayer(evaluator), MCTSPlayer())
    t_wins += wins
    t_steps += steps
    table_print(["Monte Carlo", wins, steps])
    # Alpha Beta Pruning VS PVS:
    wins, steps = run_one_experiment(AlphaBetaPlayer(evaluator), PVSPlayer(evaluator))
    t_wins += wins
    t_steps += steps
    table_print(["PVS", wins, steps])
    table_print(["Total", t_wins, t_steps])
    print()

    experiment_header_print("Principal Variation Search")
    # PVS VS Greedy:
    wins, steps = run_one_experiment(PVSPlayer(evaluator), GreedyPlayer(evaluator))
    t_wins, t_steps = wins, steps
    table_print(["Greedy", wins, steps])
    # PVS VS Alpha Beta Pruning:
    wins, steps = run_one_experiment(PVSPlayer(evaluator), AlphaBetaPlayer(evaluator))
    t_wins += wins
    t_steps += steps
    table_print(["Alpha-beta pruning", wins, steps])
    # PVS VS MCTS:
    wins, steps = run_one_experiment(PVSPlayer(evaluator), MCTSPlayer())
    t_wins += wins
    t_steps += steps
    table_print(["Monte Carlo", wins, steps])
    table_print(["Total", t_wins, t_steps])
    print()

    experiment_header_print("Monte Carlo")
    # MCTS VS Greedy:
    wins, steps = run_one_experiment(MCTSPlayer(), GreedyPlayer(evaluator))
    t_wins, t_steps = wins, steps
    table_print(["Greedy", wins, steps])
    # MCTS VS Alpha Beta Pruning:
    wins, steps = run_one_experiment(MCTSPlayer(), AlphaBetaPlayer(evaluator))
    t_wins += wins
    t_steps += steps
    table_print(["Alpha-beta pruning", wins, steps])
    # MCTS VS PVS:
    wins, steps = run_one_experiment(MCTSPlayer(), PVSPlayer(evaluator))
    t_wins += wins
    t_steps += steps
    table_print(["PVS", wins, steps])
    table_print(["Total", t_wins, t_steps])
    print()


def main() -> None:
    experiment(GreedyEvaluator)
    # experiment(ExternalEvaluator)


if __name__ == "__main__":
    main()
