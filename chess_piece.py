from pieces import PieceID


def sign(x):
    if x > 0:
        return 1
    if x == 0:
        return 0
    if x < 0:
        return -1


class ChessPiece:
    def __init__(self, color: str, piece_id: PieceID = None) -> None:
        self.color = color
        self.id = piece_id
        self.moves_list = []

    def __repr__(self) -> str:
        return self.color[0] + str(self.id.value)

    def get_moves(self) -> list[tuple[int, int]]:
        return self.moves_list

    def check_move(
            self,
            board,
            move: tuple[int, int],
            start: tuple[int, int],
            end: tuple[int, int]
    ) -> bool:
        """
        Default movement legality check for Rook, Bishop and Queen
        :param board: a board.Board object
        :param move: (x_delta, y_delta) delta = end - start
        :param start: (x_start, y_start), coordinates set that determines starting position of moved piece
        :param end: (x_end, y_end), determines ending position of moved piece
        :return: True or False, Determines legality of move
        """
        if board[end[0]][end[1]] and board[end[0]][end[1]] == self.color:
            return False
        diff = (sign(move[0]), sign(move[1]))
        x, y = move[0] - diff[0], move[1] - diff[1]

        while x != 0 or y != 0:
            if board[start[0] + x][start[1] + y]:
                return False
            x -= diff[0]
            y -= diff[1]

        return True


class Pawn(ChessPiece):
    def __init__(self, color) -> None:
        super().__init__(color, PieceID.PAWN)
        self.value = 1
        self.capture_moves_pawn = []
        self.first_moves = []
        if self.color == 'white':
            self.capture_moves_pawn = [(1, 1), (-1, 1)]
            self.moves_list = [(0, 1)]
            self.first_moves = [(0, 2)]
        else:
            self.capture_moves_pawn = [(1, -1), (-1, -1)]
            self.moves_list = [(0, -1)]
            self.first_moves = [(0, -2)]

    def check_move(self, board, move, start, end) -> bool:
        end_piece = board[end[0]][end[1]]
        if end_piece and end_piece == self.color:
            return False
        if move not in self.moves_list:
            if move not in self.first_moves:
                if move not in self.capture_moves_pawn or not end_piece:
                    return False
            elif board[start[0]][start[1] + sign(move[1])] or (start[1] != 1 and start[1] != 6):
                return False

        return not end_piece


class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color, PieceID.ROOK)
        self.value = 5
        self.moves_list = []
        for i in range(7):
            self.moves_list.append((0, i + 1))
            self.moves_list.append((0, -i - 1))
            self.moves_list.append((i + 1, 0))
            self.moves_list.append((-i - 1, 0))


class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color, PieceID.KNIGHT)
        self.value = 3
        self.moves_list = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    def check_move(self, board, move, start, end) -> bool:
        if board[end[0]][end[1]] and board[end[0]][end[1]] == self.color:
            return False
        return move in self.moves_list


class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color, PieceID.BISHOP)
        self.value = 3
        for i in range(7):
            self.moves_list.extend([(i + 1, i + 1), (i + 1, -i - 1), (-i - 1, i + 1), (-i - 1, -i - 1)])


class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color, PieceID.QUEEN)
        self.value = 5
        for i in range(7):
            self.moves_list.extend([
                (0, i + 1), (0, -i - 1), (i + 1, 0), (-i - 1, 0),
                (i + 1, i + 1), (i + 1, -i - 1), (-i - 1, i + 1), (-i - 1, -i - 1)
            ])


class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color, PieceID.KING)
        self.value = -1
        self.moves_list = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def check_move(self, board, move, start, end) -> bool:
        if board[end[0]][end[1]] and board[end[0]][end[1]] == self.color:
            print(board[end[0]][end[1]].color)
            print(self.color)
            return False
        return move in self.moves_list