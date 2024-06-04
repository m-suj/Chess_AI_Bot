from pieces import PieceID
from chess_piece import *


class Board:
    def __init__(self) -> None:
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
        self.check = None
        self.mate = None

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
                self.pieces[color + 'king'],
                self.pieces[color + 'queen'],
                self.pieces[color + 'bishop'],
                self.pieces[color + 'knight'],
                self.pieces[color + 'rook']
            )
            self.kings_positions = {'white': (3, 0), 'black': (3, 7)}

    def __getitem__(self, item: int) -> list:
        return self.board[item]

    def execute_move(self, color: str, start: str, end: str) -> bool:
        """
        Board's method for managing logic behind making a move in chess.
        :param color: 'white' or 'black'
        :param start: starting position, given by the regex format [a-hA-H][1:8]
        :param end: end position, given by the regex format [a-hA-H][1:8]
        """

        # Support variables declaration
        s, e = (ord(start[0]) - 97, int(start[1]) - 1), (ord(end[0]) - 97, int(end[1]) - 1)
        piece: ChessPiece = self[s[0]][s[1]]  # Piece standing on param:start tile, that is requested to be moved
        end_piece = self[e[0]][e[1]]  # Piece standing on param:end tile
        move = e[0] - s[0], e[1] - s[1]  # (x_delta, y_delta)

        # Check if the player is allowed to move the piece in the first place
        if not piece or piece.color != color:
            print('Cannot execute the move, try again')
            return False

        # Analyze move based on piece's movement rules
        move_status = piece.check_move(self, move=move, start=s, end=e)

        # Updating the board
        if not move_status:
            print('Cannot execute the move, try again')
            return False

        buffer = self[e[0]][e[1]]
        self[e[0]][e[1]] = self[s[0]][s[1]]
        self[s[0]][s[1]] = None
        if piece.id == PieceID.KING:
            self.kings_positions[piece.color] = e

        # Exposing your own king - move has to be undone
        own_king_exposed = self.check_detection(color)
        if own_king_exposed:
            self[s[0]][s[1]] = self[e[0]][e[1]]
            self[e[0]][e[1]] = buffer
            if piece.id == PieceID.KING:
                self.kings_positions[piece.color] = s
            print('You can\'t do this move, your king will be exposed!')
            return False

        # Checking an enemy's king - checkmate procedure
        enemy_color = 'white' if color == 'black' else 'black'
        enemy_king_checked = self.check_detection(enemy_color)
        if not enemy_king_checked:
            self.check = None
        else:
            self.check = enemy_color
            self.mate = enemy_color  # Assuming that the king is checkmated and searching for a chance to escape

            # Checking if moving the king allows to avoid 'check'
            original_king_pos = self.kings_positions[enemy_color]
            for i in range(8):
                if not self.mate:
                    break
                for j in range(8):
                    piece: ChessPiece = self[i][j]
                    if piece and piece.color == self.check:
                        moves_list = []
                        if piece.id == PieceID.PAWN:
                            moves_list.extend(piece.capture_moves_pawn)
                            if j == 1 or j == 6:
                                moves_list.extend(piece.first_moves)
                        moves_list.extend(piece.moves_list)
                        for m in moves_list:
                            if i + m[0] >= 8 or j + m[1] >= 8:
                                continue
                            if piece.check_move(self, m, (i, j), (i + m[0], j + m[1])):
                                if piece.id == PieceID.KING:
                                    self.kings_positions[enemy_color] = (i + m[0], j + m[1])
                                buffer = self[i + m[0]][j + m[1]]
                                self[i + m[0]][j + m[1]] = self[i][j]
                                self[i][j] = None

                                if not self.check_detection(enemy_color):
                                    print(f'DEBUG: Piece {piece.id} can be moved from {(i, j)} to {(i + m[0], j + m[1])} to avoid check')
                                    self.mate = None

                                if piece.id == PieceID.KING:
                                    self.kings_positions[enemy_color] = (i, j)
                                self[i][j] = self[i + m[0]][j + m[1]]
                                self[i + m[0]][j + m[1]] = buffer

                                if not self.mate:
                                    break

        print(f'Moving {s} to {e}')
        if self.mate:
            print(f'MATE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return True

    def check_detection(self, color: str) -> bool:
        # King check detection - illegal move, will return 'True' regardless of color,
        # which triggers a move undo procedure in self.execute_move
        if (
                self.kings_positions['white'][0] - self.kings_positions['black'][0],
                self.kings_positions['white'][1] - self.kings_positions['black'][1]
        ) in self.pieces['w_king'].moves_list:
            return True

        king_pos = self.kings_positions[color]

        # Pawn check detection
        side = 1 if color == 'white' else -1
        tiles = self[king_pos[0] + 1][king_pos[1] + side], self[king_pos[0] - 1][king_pos[1] + side]
        for tile in tiles:
            if tile and tile.id == PieceID.PAWN and tile.color != color:
                return True

        # Other (rook, bishop, queen, knight) check detection
        for i in range(8):
            for j in range(8):
                piece = self[i][j]
                if piece and piece.color != color and piece.id not in[PieceID.KING, PieceID.PAWN]:
                    capture_move = king_pos[0] - i, king_pos[1] - j
                    if capture_move in piece.moves_list and piece.check_move(self, capture_move, (i, j), king_pos):
                        return True

        return False


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
