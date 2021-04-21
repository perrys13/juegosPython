tablero = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
jugadoractual = "X"
juegosigue = True


def mostrartablero():
    print("|" + tablero[0] + "|" + tablero[1] + "|" + tablero[2] + "|" "   | 1 | 2 | 3 |")
    print("|" + tablero[3] + "|" + tablero[4] + "|" + tablero[5] + "|" "   | 4 | 5 | 6 |")
    print("|" + tablero[6] + "|" + tablero[7] + "|" + tablero[8] + "|" "   | 7 | 8 | 9 |")


def juego():
    global juegosigue
    mostrartablero()
    while juegosigue:
        turnos()
        hayganador()
        cambiarjugador()
        if "-" not in tablero and hayganador()==False:
            print("Empate!")
            juegosigue = False


def turnos():
    validacion = False
    jugada = input("jugador " + jugadoractual + " ingrese posicion 1-9 : ")
    while not validacion:

        while jugada not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            jugada = input("jugador " + jugadoractual + " ingrese posicion 1-9 : ")

        jugada = int(jugada) - 1

        if tablero[jugada] == "-":
            validacion = True
        else:
            print("posicion ocupada")
    tablero[jugada] = jugadoractual
    mostrartablero()


def hayganador():
    global juegosigue
    if verfilas() or vercolumnas() or verdiagonales():
        print("El ganador es el jugador " + ganador)
        juegosigue = False
        hayganador=True
    else:
        juegosigue = True
        hayganador=False
    return(hayganador)


def verfilas():
    global ganador

    if tablero[0] == tablero[1] == tablero[2] != "-":
        verfilas = True
        ganador = tablero[0]
    elif tablero[3] == tablero[4] == tablero[5] != "-":
        verfilas = True
        ganador = tablero[3]
    elif tablero[6] == tablero[7] == tablero[8] != "-":
        verfilas = True
        ganador = tablero[6]
    else:
        verfilas = False
    return (verfilas)


def vercolumnas():
    global ganador

    if tablero[0] == tablero[3] == tablero[6] != "-":
        vercolumnas = True
        ganador = tablero[0]
    elif tablero[1] == tablero[4] == tablero[7] != "-":
        vercolumnas = True
        ganador = tablero[1]
    elif tablero[2] == tablero[5] == tablero[8] != "-":
        vercolumnas = True
        ganador = tablero[2]
    else:
        vercolumnas = False
    return (vercolumnas)


def verdiagonales():
    global ganador
    if tablero[0] == tablero[4] == tablero[8] != "-":
        verdiagonales = True
        ganador = tablero[0]
    elif tablero[2] == tablero[4] == tablero[6] != "-":
        verdiagonales = True
        ganador = tablero[2]
    else:
        verdiagonales = False
    return (verdiagonales)


def cambiarjugador():
    global jugadoractual
    if jugadoractual == "X":
        jugadoractual = "O"
    else:
        jugadoractual = "X"


juego()
