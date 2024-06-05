

class Player:
    def __init__(
            self,
            name: str,
            color: str,
            ai: bool = False
    ) -> None:
        self.name = name
        self.color = color
        self.ai = ai

    def play_turn(self) -> str:
        if not self.ai:
            return input('Please enter your move (format: a1:b2): ')
        else:
            return None