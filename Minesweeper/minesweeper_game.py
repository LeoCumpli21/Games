from random import choice, randint


def validar_adyacente(tablero, idx):
    i, j = idx
    mina = 0
    for s in range(i - 1, i + 2):
        for t in range(j - 1, j + 2):
            try:
                if tablero[s][t] == -1:
                    mina += 1
                else:
                    continue
            except:
                mina += 1
    if mina < 7:
        return True
    else:
        return False


def validar_mina(tablero, idx):
    i, j = idx
    mina = 0
    for s in range(i - 1, i + 2):
        for t in range(j - 1, j + 2):
            try:
                if tablero[s][t] == -1:
                    if validar_adyacente(tablero, (s, t)):
                        mina += 1
                    else:
                        return False
                else:
                    pass
            except:
                mina += 1
    if mina < 8:
        return True
    else:
        return False


def crear_tablero(x, y):
    """Creamos la matriz del buscaminas, colocando las minas de manera
    aleatoria"""
    tablero = []
    for i in range(x):
        tablero.append([])
        for j in range(y):
            tablero[i].append(0)

    # Colocamos las minas
    for row in range(len(tablero)):
        for j in range(y):
            if validar_mina(tablero, (row, j)):
                tablero[row][j] = -1

    return tablero


def print_tablero(tablero):
    """Imprime el tablero"""
    for row in tablero:
        for col in row:
            if col == -1:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()


tab = crear_tablero(9, 9)
print_tablero(crear_tablero(9, 9))
