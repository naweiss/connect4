from connect4 import Connect4Game, Player
from players.greedy import GreedyPlayer
from players.alpha_beta import AlphaBetaPlayer
from players.pvs import PVSPlayer
from players.mcts import MCTSPlayer

GAME = Connect4Game()
EXP_TIMES = 12


def run_one_game(first_player, second_player):
    game_over = False
    moving_steps = 0

    # Game loop
    while not game_over:
        if GAME.current_player == Player.FIRST:
            current_player = first_player
        else:
            current_player = second_player

        column = current_player.choose_move()
        GAME.play_move(column)
        moving_steps += 1
        GAME.switch_turn()

        # Check game over
        game_over, winner = GAME.check_win()
        if game_over:
            return winner, moving_steps

    return None, -1


def run_one_experiment(first_player, second_player, times):
    total_moving_steps = 0
    first_player_wins = 0

    for _ in range(int(times / 2)):
        winner, current_moving_steps = run_one_game(first_player, second_player)
        total_moving_steps += current_moving_steps
        if winner is Player.FIRST:
            first_player_wins += 1
        # Alternate:
        winner, current_moving_steps = run_one_game(second_player, first_player)
        total_moving_steps += current_moving_steps
        if winner is Player.SECOND:
            first_player_wins += 1

    return first_player_wins, total_moving_steps


def main():

    # Greedy VS Alpha Beta Pruning:
    print("Greedy VS Alpha Beta Pruning:")
    wins, steps = run_one_experiment(GreedyPlayer(GAME), AlphaBetaPlayer(GAME), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Greedy VS PVS:
    print("Greedy VS PVS:")
    wins, steps = run_one_experiment(GreedyPlayer(GAME), PVSPlayer(GAME), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Greedy VS MCTS:
    print("Greedy VS MCTS:")
    wins, steps = run_one_experiment(GreedyPlayer(GAME), MCTSPlayer(GAME), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Alpha Beta Pruning VS Greedy:
    print("Alpha Beta Pruning VS Greedy:")
    wins, steps = run_one_experiment(AlphaBetaPlayer(GAME), GreedyPlayer(GAME), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Alpha Beta Pruning VS PVS:
    print("Alpha Beta Pruning VS PVS:")
    wins, steps = run_one_experiment(AlphaBetaPlayer(GAME), PVSPlayer(GAME), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # Alpha Beta Pruning VS MCTS:
    print("Alpha Beta Pruning VS MCTS:")
    wins, steps = run_one_experiment(AlphaBetaPlayer(GAME), MCTSPlayer(GAME), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # PVS VS Greedy:
    print("PVS VS Greedy:")
    wins, steps = run_one_experiment(PVSPlayer(GAME), GreedyPlayer(GAME), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # PVS VS Alpha Beta Pruning:
    print("PVS VS Alpha Beta Pruning:")
    wins, steps = run_one_experiment(PVSPlayer(GAME), AlphaBetaPlayer(GAME), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # PVS VS MCTS:
    print("PVS VS MCTS:")
    wins, steps = run_one_experiment(PVSPlayer(GAME), MCTSPlayer(GAME), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # MCTS VS Greedy:
    print("MCTS VS Greedy:")
    wins, steps = run_one_experiment(MCTSPlayer(GAME), GreedyPlayer(GAME), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # MCTS VS Alpha Beta Pruning:
    print("MCTS VS Alpha Beta Pruning:")
    wins, steps = run_one_experiment(MCTSPlayer(GAME), AlphaBetaPlayer(GAME), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()

    # MCTS VS PVS:
    print("MCTS VS PVS:")
    wins, steps = run_one_experiment(MCTSPlayer(GAME), PVSPlayer(GAME), EXP_TIMES)
    print("Greedy wins: ", wins)
    print("Moving steps: ", steps)
    print()


if __name__ == "__main__":
    main()
