
class ChessException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NoPiece(ChessException):
    def __init__(self):
        super().__init__('CANNOT EXECUTE: The piece doesn\'t exist')


class WrongPiece(ChessException):
    def __init__(self):
        super().__init__('CANNOT EXECUTE: This isn\'t your piece')


class CapturedOwnPiece(ChessException):
    def __init__(self):
        super().__init__('CANNOT EXECUTE: You cannot land on your own piece')


class InvalidMove(ChessException):
    def __init__(self):
        super().__init__('CANNOT EXECUTE: The piece cannot be moved in this way')


class GoingThroughPiece(ChessException):
    def __init__(self):
        super().__init__('CANNOT EXECUTE: You\'re trying to pass through another piece')


class KingExposed(ChessException):
    def __init__(self):
        super().__init__('CHECK DANGER: cannot execute, your king will be exposed!')


class PawnNotFirstMove(ChessException):
    def __init__(self):
        super().__init__('CANNOT EXECUTE: This pawn has been moved before, you can\'t move it by two tiles ahead')


class PawnNothingToCapture(ChessException):
    def __init__(self):
        super().__init__('CANNOT EXECUTE: The pawn is allowed to do this move only when capturing another piece')


class PawnCannotCapture(ChessException):
    def __init__(self):
        super().__init__('CANNOT EXECUTE: The pawn cannot capture with that move!')


class BelatedEnPassant(ChessException):
    def __init__(self):
        super().__init__('CANNOT EXECUTE: You are too late, you can only enpass pawns that have just moved there by two tiles')


class EnPassant(ChessException):
    def __init__(self):
        super().__init__('UNHANDLED EXCEPTION: Unusual move')


class Promotion(ChessException):
    def __init__(self):
        super().__init__('UNHANDLED EXCEPTION: Promotion')