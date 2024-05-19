from enum import Enum
from chess_piece import *


class Piece(Enum):
    PAWN = 0
    ROOK = 1
    KNIGHT = 2
    BISHOP = 3
    QUEEN = 4
    KING = 5


class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for __ in range(8)]
        # Set up the pieces
        for i in range(8):
            self.board[1][i] = Pawn('white')


    def __getitem__(self, item):
        return self.board[item]


    def draw_board(self):
        print(' ', end='')
        for i in range(8):
            print(f'|{chr(i + 65)}\t', end='')
        print('|')

        for row in range(8):
            print('_' * 33)
            print(f'{row + 1}', end='')
            for col in range(8):
                print('|', end='')

                # Print a piece
                print('' if self.board[row][col] is None else self.board[row][col], end='\t')

            print('|')

        print('_' * 33)
        print(' ', end='')
        for i in range(8):
            print(f'|{chr(i + 65)}\t', end='')
        print('|')
