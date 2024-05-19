from pieces import Piece
from chess_piece import *


class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for __ in range(8)]
        # Set up the pieces
        for i in range(8):
            self.board[1][i] = Pawn('white')
            self.board[6][i] = Pawn('black')
        for side, color in (0, 'white'), (7, 'black'):
            (
                self.board[side][0],
                self.board[side][1],
                self.board[side][2],
                self.board[side][3],
                self.board[side][4],
                self.board[side][5],
                self.board[side][6],
                self.board[side][7]
            ) = (
                Rook(color),
                Knight(color),
                Bishop(color),
                Pawn(color),  # To be replaced
                Pawn(color),  # To be replaced
                Bishop(color),
                Knight(color),
                Rook(color)
            )

    def __getitem__(self, item):
        return self.board[item]


    def draw_board(self):
        print(' ', end='')
        for i in range(7, -1, -1):
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
        for i in range(7, -1, -1):
            print(f'|{chr(i + 65)}\t', end='')
        print('|')
