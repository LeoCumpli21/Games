# Vamos a describir las funciones del juego
#Leo es muy bello
#Juego chido y fregon

def crear_tablero():
    #itera colocando minas dentro de una matriz 9*9

def validar_mina(tablero,idx):
    i,j=idx
    mina=0
    for s in range(i-1,i+2):
        for t in range(j-1,j+2): 
            try:
                if tablero[s][t]==-1:
                    mina+=1
                else:
                    return True
            except:
                mina+=1
    if mina<8:
        return True
    else:
        return False

def resolver_tablero():
    #input matriz de tablero
    #output tablero con 0 y 1

def print_tablero():
    #muestra casillas ocultas y casillas seleccionadas

def expandir_casillas():
    #revela casillas




def main():
    
























































'''def print_matriz(matriz, nombre_columnas):
    bigger_size = []
    for nombre in nombre_columnas:
        bigger_size.append(len(nombre))
    
    for idx, fila in enumerate(matriz):
        for element in fila:
            if len(str(element)) > bigger_size[idx]:
                bigger_size[idx] = len(str(element))

    for i in range(len(nombre_columnas)):
        print(nombre_columnas[i].center(bigger_size[i] + 2), end = "")
    print()
    
    for i in range(len(matriz[0])):
        for j in range(len(nombre_columnas)):
            print(str(matriz[j][i]).title().center(bigger_size[j] + 2), end = "")
        print()'''