

class ChessPiece:
    def __init__(self, color):
        self._color = color
        # self._position = position


class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.value = 1


class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.value = 5


class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.value = 3


class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.value = 3