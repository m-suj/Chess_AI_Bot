from board import Board


def main():
    b = Board()
    b.draw_board()
    b.execute_move('white', 'h1', 'e3')
    b.draw_board()


if __name__ == '__main__':
    main()
