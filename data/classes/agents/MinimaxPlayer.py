from data.classes.Square import Square
from data.classes.Board import Board
from data.classes.agents.ChessAgent import ChessAgent

import copy
import random
import math

class MinimaxPlayer(ChessAgent):
    def choose_action(self, board: Board):
        depth = 2
        if board.turn == "white":
            move = self.minimax(board, depth, True)
        else:
            move = self.minimax(board, depth, False)
        
        print(move)
        possible_moves: list[tuple[Square, Square]] = []
        for square in board.squares:
            if square.occupying_piece != None and square.occupying_piece.color == self.color:
                for target in square.occupying_piece.get_valid_moves(board):
                    possible_moves.append((square, target))
        print(possible_moves)
        return possible_moves[move[1]]
    
    
    def minimax(self, board: Board, depth: int, isMaximizing: bool, moveIndex=-1):
        # base case  
        if depth == 0 or board.is_in_checkmate("white") or board.is_in_checkmate("black"):
            return (board.get_evaluation(), moveIndex) 
        
        # maximizing player
        if isMaximizing:
            possible_boards = self.get_possible_boards(board, "white")
            maxEval = -math.inf
            for i in range(len(possible_boards)):
                eval, newIndex = self.minimax(possible_boards[i], depth - 1, False, i)
                if (maxEval <= eval):
                    maxEval = eval
                    index = newIndex
            return (maxEval, index) 

        # minimizing player
        else:
            minEval = math.inf
            possible_boards = self.get_possible_boards(board, "black")
            for i in range(len(possible_boards)):
                eval, newIndex = self.minimax(possible_boards[i], depth - 1, True, i)
                if (minEval >= eval):
                    minEval = eval
                    index = newIndex
            return (minEval, index)

        
    def get_possible_boards(self, board, color):
        # get a list of all possible moves
        possible_moves: list[tuple[Square, Square]] = []
        for square in board.squares:
            if square.occupying_piece != None and square.occupying_piece.color == color:
                for target in square.occupying_piece.get_valid_moves(board):
                    possible_moves.append((square, target))
        
        #get a list of all posible boards with those moves
        possible_boards = []
        i = 0
        for from_square, to_square in possible_moves:
            new_board = copy.deepcopy(board)
            new_board.handle_move(new_board.get_square_from_pos(from_square.pos), new_board.get_square_from_pos(to_square.pos))
            possible_boards.append(new_board)

            # print(from_square.occupying_piece.notation, to_square.occupying_piece)
            # print("eval: ", new_board.get_evaluation(), "\nindex: ", i)
            # new_board.print_state()

            i += 1

            
        # print("-------------------------------------------------")

        return possible_boards