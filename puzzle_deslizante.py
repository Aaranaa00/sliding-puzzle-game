from random import shuffle

DIMENSION_TABLERO = 3
FICHA = ""

def crear_numeros_puzzle():
    """Genera una lista de números del 1 al tamaño del tablero (sin incluir el espacio vacío)"""
    return [x for x in range(1, DIMENSION_TABLERO**2 +1)]

def crear_tablero(cant_numeros):
    """Convierte la lista de números en un tablero 2D, reemplazando el último número con el espacio vacío"""
    matriz = []
    indice = 0
    
    for _ in range(DIMENSION_TABLERO):
        fila = []
        for _ in range(DIMENSION_TABLERO):
            if cant_numeros[indice] == DIMENSION_TABLERO**2:
                cant_numeros[indice] = FICHA
                
            fila.append(cant_numeros[indice])
            indice += 1
        matriz.append(fila)
        
    return matriz

def comprobar_victoria(matriz_resultante, matriz_usuario):
    """Verifica si el tablero del jugador equivale al tablero resultante"""
    return all(matriz_resultante[x] == matriz_usuario[x] for x in range(DIMENSION_TABLERO))

def buscar_blanco(matriz):
    """Encuentra la posición del espacio vacío (FICHA) en el tablero"""
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] == FICHA:
                return f, c

def imprimir_tablero(tablero):
    """Imprime el tablero de juego en formato visual amigable"""
    for fila in tablero:
        print(("+------" * DIMENSION_TABLERO) + "+")
        print(("|      " * DIMENSION_TABLERO) + "|")
        for num in fila:
            print(f'|  {num : >2}  ', end="")
        print("|")
        print(("|      " * DIMENSION_TABLERO) + "|")
    print(("+------" * DIMENSION_TABLERO) + "+")
    
def buscar_posibles_movimientos(tablero):
    """Determina qué movimientos son posibles para el jugador según la posición del espacio vacío"""
    fila, columna = buscar_blanco(tablero)
    arriba, abajo, derecha, izq = True, True, True, True
    if fila == 0:
        arriba = False
    if fila == DIMENSION_TABLERO -1:
        abajo = False
    if columna == 0:
        izq = False
    if columna == DIMENSION_TABLERO -1:
        derecha = False 
    
    return izq, derecha, arriba, abajo

def pintar_movimientos(izquierda, derecha, arriba, abajo):
    """Muestra en pantalla los movimientos disponibles para el jugador en función de la posición del espacio vacío"""
    if arriba:
        print("    (W)")
    else:
        print("    ( )")
  
    if izquierda:
        print("(A)", end=" ")
    else:
        print("( )",end=" ")
        
    if abajo:
        print("(S)", end=" ")
    else:
        print("( )",end=" ")
    
    if derecha:
        print("(D)", end=" ")
    else:
        print("( )",end=" ")
    
    print("or quit")

def mover_posicion(tablero, letra):
    """Mueve el espacio vacío en el tablero según la letra ingresada por el jugador (W, A, S, D)"""
    f, c = buscar_blanco(tablero)
    es_movido = True
    match letra:
        case "s":
            if f == DIMENSION_TABLERO -1:
                es_movido = False
            else:
                tablero[f][c], tablero[f+1][c] = tablero[f+1][c], tablero[f][c]
        case "w":
            if f == 0:
                es_movido = False
            else:
                tablero[f][c], tablero[f-1][c] = tablero[f-1][c], tablero[f][c]
        case "a":
            if c == 0:
                es_movido = False
            else:
                tablero[f][c], tablero[f][c-1] = tablero[f][c-1], tablero[f][c]
        case "d":
            if c == DIMENSION_TABLERO -1:
                es_movido = False
            else:
                tablero[f][c], tablero[f][c+1] = tablero[f][c+1], tablero[f][c]
        case _:
            es_movido = False
    
    return es_movido

def jugar():
    """Inicia y controla el flujo principal del juego Puzle Deslizante"""
    print("Bienvenido al Puzle Deslizante.")
    print("------------------------------")
    numeros = crear_numeros_puzzle()
    tablero_resultado = crear_tablero(numeros)
    shuffle(numeros)
    tablero_jugado = crear_tablero(numeros)
    letra = ""

    while not comprobar_victoria(tablero_resultado, tablero_jugado) and letra != "quit":
        imprimir_tablero(tablero_jugado)
        izq, der, arriba, abajo = buscar_posibles_movimientos(tablero_jugado)
        
        movimiento_producido = False
        pintar_movimientos(izq, der, arriba, abajo)
        
        while not movimiento_producido and letra != "quit":
            letra = input("> ").lower()
            
            movimiento_producido = mover_posicion(tablero_jugado, letra)
            
            if not movimiento_producido and letra != "quit":
                print("Letra erronea. Elige de nuevo")  
        print()

    if comprobar_victoria(tablero_resultado, tablero_jugado):
        imprimir_tablero(tablero_resultado)
        print("Enhorabuena, has conseguido completar correctamente el puzle")
    else:
        print("Abandonando Puzle Deslizante...")
        
    print("Hasta la próxima!")
if __name__ == "__main__":
    jugar()