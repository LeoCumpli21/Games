board1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

board2 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


def solve(bo):
    """The algorith that's gonna backtrack"""
    find = find_empty(bo)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def is_valid(bo, num, pos):
    """Returns bollean expresion whether inserting some number
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


def print_board(bo):
    print("0 1 2  3 4 5  6 7 8 \n \n")
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(
                    str(bo[i][j]) + "    ", str(i)
                )  # When it prints the 9th element of a row, inserts a \n
            else:  # Otherwhise, remains in the same line
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    """Returns a tuple (row, col) with the coordinates of an
    empty space on the board"""

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


def ask_user():
    """Asks the user for the row, col, and val to insert on the
    sudoku"""

    row, col, val = tuple(
        [
            int(elem)
            for elem in input(
                """Give the coordenates and value to insert on the sudoku, 
        with the form row, col, val: \n"""
            ).split(",")
        ]
    )
    return row, col, val


def insert_value(row, col, val, bo):
    bo[row][col] = val

    return bo


# Computer solves board 1
solve(board1)

# This while loop ends when the board is completed
# correctly by the user
while board2 != board1:

    print_board(board2)
    row, col, val = ask_user()
    insert_value(row, col, val, board2)

print_board(board2)
print("""Congrats, You've completed the sudoku board successfully""")
