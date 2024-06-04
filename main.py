from game import Game


def main():
    game = Game()
    while not game.winner:
        game.draw_board()
        game.play_turn()
    game.draw_board()


if __name__ == '__main__':
    main()
