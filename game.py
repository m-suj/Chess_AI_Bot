from board import Board
from player import Player
from re import match
from chess_move_exceptions import ChessException


class Game:
    def __init__(self):
        self.move_pattern = r'^[a-hA-H][1-8]:[a-hA-H][1-8]$'
        self.coord_pattern = r'^[a-hA-H][1-8]$'
        self.board = Board()

        # Players
        self.player_1 = Player('Player1', 'white')
        self.player_2 = Player('Player2', 'black')
        self.turn = self.player_1  # active player

        # Game state
        self.winner = None
        self.moves_log: list[tuple[str, str]] = []

    def draw_board(self):
        self.board.draw_board()
        self.print_game_state()

    def print_game_state(self):
        if self.moves_log:
            piece = self.moves_log[-1][0]
            move = self.moves_log[-1][1]
            start, end = move[:2], move[3:5]
            print(f'Piece \'{piece}\' moved from {start} to {end}')
        else:
            print(
                f'GAME OF CHESS. '
                f'PLAYER \'{self.player_1.name}\'({self.player_1.color}, {'bot' if self.player_1.ai else 'human'}) VS '
                f'PLAYER \'{self.player_2.name}\'({self.player_2.color}, {'bot' if self.player_1.ai else 'human'}). \n'
                f'GOOD LUCK!\n')

        if self.winner:
            print(f'CHECKMATE! PLAYER {self.winner.name} ({self.winner.color}) WINS!')
        else:
            if self.board.check:
                print('CHECK!!!')
            print(f'{self.turn.color.capitalize()}\'s turn')


    def play_turn(self):
        """Function responsible for main game loop, executing it plays an entire active player's turn
        and switches to the next player"""
        move_status = False
        while not move_status:
            # Checking validity of the move
            move: str = self.turn.play_turn()
            move_status = True
            if match(self.move_pattern, move):
                move = move.lower()
                try:
                    piece = self.board.execute_move(self.turn.color, move[:2], move[3:5])
                    self.moves_log.append((piece, move))
                except ChessException as e:
                    print(e.args[0])
                    move_status = False
            else:
                # Incorrect input format from player
                print('This isn\'t a valid move format, please try again')
                move_status = False

        # Checkmate?
        if self.board.mate:
            self.winner = self.turn

        # Next player
        if self.turn is self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1