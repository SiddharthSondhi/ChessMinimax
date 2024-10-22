# /* Square.py

from __future__ import annotations
import pygame

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data.classes.Piece import Piece

import copy

# Tile creator
class Square:
    def __init__(self, x: int, y: int, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.abs_x = x * width
        self.abs_y = y * height
        self.abs_pos = (self.abs_x, self.abs_y)
        self.pos = (x, y)
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.draw_color = (255, 180, 140) if self.color == 'light' else (180, 140, 255)
        self.highlight_color = (180, 255, 100) if self.color == 'light' else (140, 200, 80)
        self.occupying_piece: Piece = None
        self.coord = self.get_coord()
        self.highlight = False
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )

    # get the formal notation of the tile
    def get_coord(self) -> str:
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)

    def draw(self, display: pygame.surface.Surface) -> None:
        # configures if tile should be light or dark or highlighted tile
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)
        # adds the chess piece icons
        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)
    
    # used for deep copying without copying extra pygame stuff
    def __deepcopy__(self, memo):
        new_inst = type(self).__new__(self.__class__)
        new_inst.x = self.x
        new_inst.y  = self.y
        new_inst.width = self.width
        new_inst.height = self.height
        new_inst.abs_x = self.abs_x
        new_inst.abs_y = self.abs_y
        new_inst.abs_pos = copy.deepcopy(self.abs_pos, memo)
        new_inst.pos = copy.deepcopy(self.pos, memo)
        new_inst.color = self.color
        new_inst.draw_color = copy.deepcopy(self.draw_color, memo)
        new_inst.highlight_color = copy.deepcopy(self.highlight_color, memo)
        new_inst.occupying_piece = copy.deepcopy(self.occupying_piece, memo)
        new_inst.coord = copy.deepcopy(self.coord, memo)
        new_inst.highlight = self.highlight
        new_inst.rect = None


        return new_inst