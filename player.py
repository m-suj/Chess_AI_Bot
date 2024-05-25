

class Player:
    def __init__(self, color: str, ai: bool = False) -> None:
        self.color = color
        self.ai = ai

    def play_turn(self):
        if not self.ai:
            return input('Please enter your move (format: a1:b2): ')

        else:
            return -1