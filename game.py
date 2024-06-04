from board import Board
from player import Player
from re import match


class Game:
    def __init__(self):
        self.move_pattern = r'^[a-hA-H][1-8]:[a-hA-H][1-8]$'
        self.board = Board()
        # Players
        self.player_1 = Player('white')
        self.player_2 = Player('black')
        self.turn = self.player_1  # active player

        # Game state
        self.winner = None

    def draw_board(self):
        self.board.draw_board()
        if self.winner:
            print(f'Player {self.winner.color} wins!!!!!')
        else:
            if self.board.check:
                print('Check!')
            print(f'{self.turn.color.capitalize()}\'s turn')

    def play_turn(self):
        """Function responsible for main game loop, executing it plays an entire active player's turn
        and switches to the next player"""
        move_status = False
        while not move_status:
            # Board checks legality of the move and returns 0 in case of a successfully executed move, and -1 otherwise
            # Appropriate feedback messages are implemented in board's method
            move: str = self.turn.play_turn()
            if match(self.move_pattern, move):
                move = move.lower()
                move_status = self.board.execute_move(self.turn.color, move[:2], move[3:5])
            else:
                print('This isn\'t a valid move format, please try again')

        # Checkmate?
        if self.board.mate:
            self.winner = self.turn

        # Next player
        if self.turn is self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1