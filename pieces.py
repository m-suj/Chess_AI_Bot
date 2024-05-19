from enum import Enum


class Piece(Enum):
    """
    Debug signs for easier identification and stdout representation of pieces on the board.
    Main purpose is for easier and more efficient comparison between piece objects (regardless of their color).
    """
    PAWN = '_p'
    ROOK = '_r'
    KNIGHT = '_k'
    BISHOP = '_b'
    QUEEN = '_q'
    KING = '_m'