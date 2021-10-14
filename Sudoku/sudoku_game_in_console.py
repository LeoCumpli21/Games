import os
from random import choice


def limpia():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


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
        """\nGive the coordenates and value to insert on the sudoku, 
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

    if (row, col) in non_zero:
        return True
    return False


def insert_value(row, col, val, bo):
    """Inserts the given value into the board in the given coordinates"""

    bo[row][col] = val
    return bo


boards_file = open("boards.txt", "r")
boards = boards_file.readlines()

solved_board = []
user_board = []


inicio = int(input("\nPress 1 to begin, or any other key to stop the game: "))

if inicio == 1:
    limpia()
    print("\Modes:")
    print("\n1.- Easy.")
    print("\n2.- Intermediate.")
    print("\n3.- Hard.")
    valid = False
    # Verificar que el usuario elija mode adecuada
    while not valid:

        mode = input("\nElija la mode que desea (introduzca el número): ")
        try:
            mode = int(mode)
        except:
            print("Ingrese el número de la mode\n")
            continue

        chosen_board = None
        # Elejir un chosen_board de cierta mode de manera aleatoria.
        if mode == 1:
            chosen_board = choice(boards[:3]).rstrip().replace(" ", "")
            pista = 0
        elif mode == 2:
            chosen_board = choice(boards[3:6]).rstrip().replace(" ", "")
            pista = 0
        elif mode == 3:
            chosen_board = choice(boards[6:]).rstrip().replace(" ", "")
        else:
            print("Dificultad inválida, inténtelo de nuevo\n")
            continue
        # Formateamos el chosen_board para poder iterar sobre él
        chosen_board = chosen_board[chosen_board.find("[") :]
        chosen_board = chosen_board.split(",")
        chosen_board = "".join(chosen_board)[1:-1].split("[")[1:]
        # Creamos la matriz que completará la computadora
        for elem in chosen_board:
            ren = []
            for num in elem:
                if num != "]":
                    ren.append(int(num))
            solved_board.append(ren)
        # Misma matriz -> esta la completa el usuario
        for elem in chosen_board:
            ren = []
            for num in elem:
                if num != "]":
                    ren.append(int(num))
            user_board.append(ren)

        valid = True
    limpia()
else:
    limpia()
    quit()

boards_file.close()

# Coordinates on the board that have non zero values
non_zero = [
    (i, j)
    for i in range(len(user_board))
    for j in range(len(user_board))
    if user_board[i][j] != 0
]

# Computer solves board 1
solve(solved_board)

# This while loop ends when user_board is completed
# correctly by the user
# Completed means equal to solved_board
while user_board != solved_board:
    print_board(user_board)
    row, col, val = ask_user()

    if is_on_board(row, col):
        print("\nThat coordinate is blocked; try again")
    else:
        insert_value(row, col, val, user_board)

print_board(user_board)
print("""Congrats, You've completed the sudoku board successfully""")
