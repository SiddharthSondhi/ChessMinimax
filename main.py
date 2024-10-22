import argparse

from data.classes.ChessMatch import chess_match
from data.classes.agents.RandomPlayer import RandomPlayer
from data.classes.agents.HumanPlayer import HumanPlayer
from data.classes.agents.ChessAgent import ChessAgent
from data.classes.agents.MinimaxPlayer import MinimaxPlayer

def main():
    num_depth_1_trials = 85
    num_depth_2_trials = 15


    parser = argparse.ArgumentParser(description="Initialize players for the game.")
    parser.add_argument('white', type=str, help="Type of the white player")
    parser.add_argument('black', type=str, help="type of the black player")
    parser.add_argument('run_eval', type=str, help="True or False if you want to run the evaluation")
    args = parser.parse_args()
    if args.white not in globals().keys():
        print(f'White player {args.white} not found!')
        return
    if args.black not in globals().keys():
        print(f'Black player {args.black} not found!')
        return
    print(args.run_eval)

    if(args.run_eval != "True"):
        white_player: ChessAgent = globals()[args.white]('white')
        black_player: ChessAgent = globals()[args.black]('black')
        chess_match(white_player, black_player)
    else:
        print("-----------------------------MINIMAX DEPTH 1 TRIALS--------------------")
        white_player = MinimaxPlayer("white", 1)
        black_player = RandomPlayer("black")
        wins = 0
        losses = 0
        draws = 0
        totalMovesNoDraws = 0
        totalMoves = 0
        for i in range(0, num_depth_1_trials):
            result, moves, totalTime = chess_match(white_player, black_player)
            if result == "white":
                wins += 1
                totalMovesNoDraws += moves
                totalMoves += moves
            elif result == "black":
                losses += 1
                totalMovesNoDraws += moves
                totalMoves += moves
            elif result == "draw":
                draws += 1
                totalMoves += moves
        print("Total Number of Depth 1 Trials:", num_depth_1_trials,
              "\nTotal wins: ", wins, "/ ", num_depth_1_trials, ", Win Rate: ", (wins / num_depth_1_trials) * 100, 
              "\nTotal Losses: ", losses, "/ ", num_depth_1_trials, ", Loss Rate: ", (losses / num_depth_1_trials) * 100,
              "\nTotal Draws: ", draws, "/ ", num_depth_1_trials, ", Draw Rate: ", (draws / num_depth_1_trials) * 100,
              "\nAvg Moves Taken to End Game(not including draws):", totalMovesNoDraws / (num_depth_1_trials - draws),
              "\nAvg Time Taken per Move: ", float(totalTime)/float(totalMoves), " seconds")

        print("---------------------------------------------------------------------------\n")

        print("-----------------------------MINIMAX DEPTH 2 TRIALS--------------------")
        white_player = MinimaxPlayer("white", 2)
        black_player = RandomPlayer("black")
        wins = 0
        losses = 0
        draws = 0
        totalMovesNoDraws = 0
        totalMoves = 0
        for i in range(0, num_depth_2_trials):
            result, moves, totalTime = chess_match(white_player, black_player)
            if result == "white":
                wins += 1
                totalMovesNoDraws += moves
                totalMoves += moves
            elif result == "black":
                losses += 1
                totalMovesNoDraws += moves
                totalMoves += moves
            elif result == "draw":
                draws += 1
                totalMoves += moves
        print("Total Number of Depth 2 Trials:", num_depth_2_trials,
              "\nTotal wins: ", wins, "/ ", num_depth_2_trials, ", Win Rate: ", (wins / num_depth_2_trials) * 100, 
              "\nTotal Losses: ", losses, "/ ", num_depth_2_trials, ", Loss Rate: ", (losses / num_depth_2_trials) * 100,
              "\nTotal Draws: ", draws, "/ ", num_depth_2_trials, ", Draw Rate: ", (draws / num_depth_2_trials) * 100,
              "\nAvg Moves Taken to End Game(not including draws):", totalMovesNoDraws / (num_depth_2_trials - draws),
              "\nAvg Time Taken per Move: ", float(totalTime)/float(totalMoves), " seconds")

        print("---------------------------------------------------------------------------\n")
        


if __name__ == '__main__':
    main()