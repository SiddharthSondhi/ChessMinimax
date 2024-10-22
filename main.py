import argparse

from data.classes.ChessMatch import chess_match
from data.classes.agents.RandomPlayer import RandomPlayer
from data.classes.agents.HumanPlayer import HumanPlayer
from data.classes.agents.ChessAgent import ChessAgent
from data.classes.agents.MinimaxPlayer import MinimaxPlayer

def main():
    parser = argparse.ArgumentParser(description="Initialize players for the game.")
    parser.add_argument('white', type=str, help="Type of the white player")
    parser.add_argument('black', type=str, help="type of the black player")
    parser.add_argument('run_eval', type=bool, help="True or False if you want to run the evaluation")
    args = parser.parse_args()
    if args.white not in globals().keys():
        print(f'White player {args.white} not found!')
        return
    if args.black not in globals().keys():
        print(f'Black player {args.black} not found!')
        return
    
    if(not args.run_eval):
        white_player: ChessAgent = globals()[args.white]('white')
        black_player: ChessAgent = globals()[args.black]('black')
        chess_match(white_player, black_player)
    else:
        print("HERE")

if __name__ == '__main__':
    main()