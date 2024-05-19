from pieces import Piece


class ChessPiece:
    def __init__(self, color, piece_id=None) -> None:
        self.color = color
        self.id = piece_id
        self.moves_list = []

    def __repr__(self) -> str:
        return str(self.id.value)

    def get_moves(self) -> list[tuple[int, int]]:
        return self.moves_list


class Pawn(ChessPiece):
    def __init__(self, color) -> None:
        super().__init__(color, Piece.PAWN)
        self.value = 1
        if self.color == 'white':
            self.moves_list = [(0, 1)]
        else:
            self.moves_list = [(0, -1)]


class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color, Piece.ROOK)
        self.value = 5
        self.moves_list = []
        for i in range(8):
            self.moves_list.append((0, i + 1))
            self.moves_list.append((0, -i - 1))
            self.moves_list.append((i + 1, 0))
            self.moves_list.append((-i - 1, 0))


class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color, Piece.KNIGHT)
        self.value = 3
        self.moves_list = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color, Piece.BISHOP)
        self.value = 3
        for i in range(8):
            self.moves_list.extend([(i + 1, i + 1), (i + 1, -i - 1), (-i - 1, i + 1), (-i - 1, -i - 1)])
