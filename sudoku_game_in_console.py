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

# dictionarie whose keys are the coordinates of
# the elmts in board that are different to 0

db = {}

for i in range(len(board2)):
    for j in range(len(board2)):
        if board2[i][j] != 0:
            db[(i, j)] = board2[i][j]


def solve(bo):
    """The algorithm that's gonna backtrack"""
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


def is_valid_input(s_input):
    """Returns True if s_input is in the correct format.
    i.e. 'row, col, val'. If not, returns false."""

    try:
        row, col, val = tuple([int(elem) for elem in s_input.split(",")])
    except:
        return False
    if (row < 0 or row > 8) or (col < 0 or col > 8) or (val < 1 or val > 9):
        return False
    return True


def ask_user():
    """Asks the user for the row, col, and val to insert on the
    sudoku."""

    user_input = input(
        """Give the coordenates and value to insert on the sudoku, 
    with the form row, col, val: \n"""
    )
    valid = is_valid_input(user_input)

    while not valid:
        user_input = input(
            """Incorrect input. Please enter it with the form row, col, val\n"""
        )
        valid = is_valid_input(user_input)

    row, col, val = tuple([int(elem) for elem in user_input.split(",")])
    return row, col, val


def is_on_board(row, col):
    """Checks whether in the given coordinates is a blocked value.
    A blocked value is a value different from 0 already on the board
    when the game started."""

    if (row, col) in db:
        return True
    return False


def insert_value(row, col, val, bo):
    """Inserts the given value into the board on the given coordinates"""

    bo[row][col] = val
    return bo


# Computer solves board 1
solve(board1)

# This while loop ends when board2 is completed
# correctly by the user
# Completed means equal to board1
while board2 != board1:
    print_board(board2)
    row, col, val = ask_user()

    if is_on_board(row, col):
        print("\nThat coordinate is blocked; try again")
    else:
        insert_value(row, col, val, board2)

print_board(board2)
print("""Congrats, You've completed the sudoku board successfully""")
