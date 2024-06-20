import chess
import chess.engine


class Player:
    def __init__(
            self,
            name: str,
            color: str,
            ai: bool = False
    ) -> None:
        self.name = name
        self.color = color
        self.is_ai = ai

        self.board: chess.Board() = None
        self.ai_engine = self.ai_setup()

    def ai_setup(self):
        if not self.is_ai:
            return None
        engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-windows-x86-64.exe")
        self.board = chess.Board()
        # Castling not implemented
        self.board.castling_rights = 0
        return engine

    def get_best_move(self, b):
        result = self.ai_engine.play(b, chess.engine.Limit(time=0.1))
        return result.move

    def play_turn(self, prev_move=None) -> str:
        if not self.ai_engine:
            return input('Please enter your move (format: a1:b2): ')
        else:
            if prev_move:
                prev = self.board.parse_uci(prev_move)
                self.board.push(prev)
            move = self.get_best_move(self.board)
            print(move)
            print(self.board)
            self.board.push(move)
            move_str = str(move)
            return move_str[0:2] + ':' + move_str[2:]

