import pygame

from data.classes.Board import Board
from data.classes.agents.ChessAgent import ChessAgent

import time

def chess_match(white_player: ChessAgent, black_player: ChessAgent):
    assert(white_player.color == 'white')
    assert(black_player.color == 'black')
    pygame.init()
    WINDOW_SIZE = (600, 600)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    board = Board(screen, WINDOW_SIZE[0], WINDOW_SIZE[1])
    agents: list[ChessAgent] = [white_player, black_player]
    i: int = 0
    moves_count: int = 0

    # Run the main game loop
    running = True
    while running:
        total_time = 0
        start = time.time()
        chosen_action = agents[i].choose_action(board)
        end = time.time()
        if (i % 2 == 0):
            total_time += end - start

        i = (i + 1) % len(agents)
        moves_count += 1
        if chosen_action == False or moves_count > 1000:
            print('Players draw!\t\t', end="\r")
            return ("draw", moves_count, total_time)
        elif not board.handle_move(*chosen_action):
            print("Invalid move!")
        elif board.is_in_checkmate(board.turn):
            if board.turn == 'white':
                print('Black wins!    ', end="\r")
                return ("black", moves_count, total_time)
            else:
                print('White wins!    ', end="\r")
                return ("white", moves_count, total_time)
        board.draw()

    # Allow the player to view the result
    viewing = True
    while viewing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                viewing = False