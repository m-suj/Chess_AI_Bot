from pieces import Piece
from chess_piece import *


def sign(x):
    if x > 0:
        return 1
    if x == 0:
        return 0
    if x < 0:
        return -1


class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for __ in range(8)]
        self.pieces = {
            'w_pawn': Pawn('white'),
            'b_pawn': Pawn('black'),
            'w_rook': Rook('white'),
            'b_rook': Rook('black'),
            'w_knight': Knight('white'),
            'b_knight': Knight('black'),
            'w_bishop': Bishop('white'),
            'b_bishop': Bishop('black'),
            'w_queen': Queen('white'),
            'b_queen': Queen('black'),
            'w_king': King('white'),
            'b_king': King('black')
            # Queen and King to be added
        }

        # Set up the pieces
        for i in range(8):
            self.board[i][1] = self.pieces['w_pawn']
            self.board[i][6] = self.pieces['b_pawn']
        for side, color in (0, 'w_'), (7, 'b_'):
            (
                self.board[0][side],
                self.board[1][side],
                self.board[2][side],
                self.board[3][side],
                self.board[4][side],
                self.board[5][side],
                self.board[6][side],
                self.board[7][side]
            ) = (
                self.pieces[color + 'rook'],
                self.pieces[color + 'knight'],
                self.pieces[color + 'bishop'],
                self.pieces[color + 'king'],  # To be replaced
                self.pieces[color + 'queen'],  # To be replaced
                self.pieces[color + 'bishop'],
                self.pieces[color + 'knight'],
                self.pieces[color + 'rook']
            )

    def __getitem__(self, item):
        return self.board[item]


    def execute_move(self, color, start, end):
        """Start/End format: 2-letter strings describing the position on the board: {'a-h'+'1-8'}"""
        # TODO: Movement logic, for now it is very simple, mostly started to test out managing pieces on the board
        s, e = (ord(start[0]) - 97, int(start[1]) - 1), (ord(end[0]) - 97, int(end[1]) - 1)
        piece = self[s[0]][s[1]]
        end_piece = self[e[0]][e[1]]
        move = e[0] - s[0], e[1] - s[1]

        if not piece or piece.color != color or (end_piece and end_piece.color == color):
            print('Cannot execute the move, try again')
            return -1
        if move not in piece.moves_list:
            # Checking if the move is a pawn capturing an opponent's piece or a pawn moving two tiles in its first move
            if piece.id == Piece.PAWN:
                if (s[1] != 1 or move[1]) != 2 and (s[1] != 6 or move[1] != -2):
                    if move not in piece.capture_moves_pawn or not end_piece:
                        print('Cannot execute the move, try again')
                        return -1
                elif self[s[0]][s[1] + sign(move[1])]:
                    print('Cannot execute the move, try again')
                    return -1
            else:
                print('Cannot execute the move, try again')
                return -1
        else:
            if piece.id == Piece.PAWN and end_piece:
                print('Cannot execute the move, try again')
                return -1
            if piece.id == Piece.ROOK or piece.id == Piece.BISHOP or piece.id == Piece.QUEEN:
                diff = (sign(move[0]), sign(move[1]))
                x, y = move[0] - diff[0], move[1] - diff[1]

                while x != 0 or y != 0:
                    if self[s[0] + x][s[1] + y]:
                        print(f'{move=}')
                        print(f'{s=}')
                        print(f'{e=}')
                        print(f'{x=}, {y=}')
                        print(self[x][y])
                        print('Cannot execute the move, try again')
                        return -1
                    x -= diff[0]
                    y -= diff[1]

        self[e[0]][e[1]] = self[s[0]][s[1]]
        self[s[0]][s[1]] = None
        print(f'Moving {s} to {e}')
        return 0


    def draw_board(self):
        print('/'*47, end='\n\n\n')
        print('\t', end='')
        for i in range(7, -1, -1):
            print(f'|{chr(i + 65)}\t', end='')
        print('|')

        for row in range(8):
            print('_' * 37)
            print(f'{row + 1}', end='\t')
            for col in range(7, -1, -1):
                print('|', end='')

                # Print a piece
                print('' if self.board[col][row] is None else self.board[col][row], end='\t')

            print('|')

        print('_' * 37)
        print('\t', end='')
        for i in range(7, -1, -1):
            print(f'|{chr(i + 65)}\t', end='')
        print('|', end='\n\n\n')
