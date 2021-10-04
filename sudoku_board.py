# Generates a random sudoku board

from random import randint
from random import choice


def random_board():
    """Generates a random sudoku board"""

    board = [list(range(9)) for i in range(9)]

    for row in range(len(board)):
        for col in range(len(board)):
            board[row][col] = 0

    for row in range(len(board)):
        for col in range(randint(4, 8)):
            col2 = choice(range(0, 9))
            board[row][col2] = randint(1, 9)

    return board


print(random_board())
