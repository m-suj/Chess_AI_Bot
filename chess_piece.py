from pieces import Piece


class ChessPiece:
    def __init__(self, color, piece_id=None):
        self._color = color
        self.id = piece_id


    def __repr__(self):
        return str(self.id.value)


class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color, Piece.PAWN)
        self.value = 1


class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color, Piece.ROOK)
        self.value = 5


class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color, Piece.KNIGHT)
        self.value = 3


class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color, Piece.BISHOP)
        self.value = 3