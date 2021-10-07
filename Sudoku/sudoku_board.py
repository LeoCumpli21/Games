# Generates a random sudoku board

from random import randint
from random import choice


def is_valid(bo, num, pos):
    """Returns boolean expresion whether inserting some number
    in an empty space is valid or not"""

    # Check whether the number is already in the current row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check whether the number is already in the current column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check whether the number is already in the current box
    box_X_coo = pos[1] // 3  # Will be an integer from 0-2
    box_Y_coo = pos[0] // 3

    for i in range(box_Y_coo * 3, box_Y_coo * 3 + 3):
        for j in range(box_X_coo * 3, box_X_coo * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def random_board():
    """Generates a random sudoku board"""

    board = [list(range(9)) for i in range(9)]

    for row in range(len(board)):
        for col in range(len(board)):
            board[row][col] = 0

    for row in range(len(board)):
        for col in range(randint(4, 9)):
            col2 = choice(range(0, 9))
            val = randint(1, 9)
            if is_valid(board, val, (row, col2)):
                board[row][col2] = val

    return board


print(random_board())
