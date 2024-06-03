from enum import Enum


class PieceID(Enum):
    """
    Debug signs for easier identification and stdout representation of pieces on the board.
    Main purpose is for easier and more efficient comparison between piece objects (regardless of their color).
    """
    PAWN = 'p'
    ROOK = 'r'
    KNIGHT = 'k'
    BISHOP = 'b'
    QUEEN = 'q'
    KING = 'm'