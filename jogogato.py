import random

def mostrar_tablero(tablero):
    print("  Tablero:")
    print(f"  {tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("  ---------")
    print(f"  {tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("  ---------")
    print(f"  {tablero[6]} | {tablero[7]} | {tablero[8]}")

def verificar_victoria(tablero, jugador):
    jugadas_de_victoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for comb in jugadas_de_victoria:
        if all(tablero[i] == jugador for i in comb): # verifica si son jugadas victoriosas 
            return True
    

def obtener_movimiento_jugador(jugador):
    while True:
        entrada = input(f"Jugador {jugador}: selecciona una casilla (1-9): ")
        if entrada.isdigit(): # verifica si es un numero del 1 a 9 
            mov = int(entrada) - 1
            if 0 <= mov <= 8:
                return mov
            else:
                print("introduce un numero del 1 al 9")
        else:
            print("introduce un numero del 1 al 9.")

def movimiento_bot(tablero):
    movimientos_disponibles = [i for i in range(9) if tablero[i] == " "] # jugadas disponibles
    
    if movimientos_disponibles:
        return random.choice(movimientos_disponibles) # retorna jugada disponible aleatoria 

def jugar_gato():
    print("El gato Contra el bot")
    tablero = [" "] * 9
    jugadores = ['X', 'O']
    turno_actual = 0
    jugando = True
    
    while jugando:
        mostrar_tablero(tablero)
        jugador_actual = jugadores[turno_actual]#jugador que le toca
        
        if jugador_actual == 'X':
            mov = obtener_movimiento_jugador('X')#moviemiento del jugador
        else:
            mov = movimiento_bot(tablero)
            print(f"el bot  (O) elige la casilla {mov + 1}")

        if tablero[mov] == " ":# verifica si la casilla esta disponible
            tablero[mov] = jugador_actual 
        else:
            print("Casilla ocupada")
            continue

        if verificar_victoria(tablero, jugador_actual):# verifica si esque gano 
            mostrar_tablero(tablero)
            if jugador_actual == 'X':
                print("ganaste contra el bot")
            else:
                print("El Bot ha ganado")
            jugando = False
        elif " " not in tablero:
            mostrar_tablero(tablero)
            print("Empate")
            jugando = False
        
        turno_actual = 1 - turno_actual # cambio de jugador

def menu_principal():
    while True:
        print("Menu Principal  ")
        print("1- 1 VS Bot  : ")
        print("2- 1 vs 1 ")
        print("3- Salir")
        opcion = input("elige una opcion 1-2-3: ")

        if opcion == '1':
            jugar_gato()
        elif opcion == '2':
            jugar_gato_1vs1()
        elif opcion == '3':
            print("saliste del juego")
            break
        else:
            print("opcion no valida")

def jugar_gato_1vs1():
    print("El gato contra amigo ")
    tablero = [" "] * 9
    jugadores = ['X', 'O']
    turno_actual = 0
    jugando = True
    
    while jugando:
        mostrar_tablero(tablero)
        jugador_actual = jugadores[turno_actual] #jugador que le toca
        
        mov = obtener_movimiento_jugador(jugador_actual) #moviemiento del jugador

        if tablero[mov] == " ": # verifica si la casilla esta disponible
            tablero[mov] = jugador_actual
        else:
            print("Casilla ocupada")
            continue

        if verificar_victoria(tablero, jugador_actual): # verifica si esque gano
            mostrar_tablero(tablero)
            print(f"Jugador {jugador_actual} ha ganado") # jugador que gano
            break 
        elif " " not in tablero:
            mostrar_tablero(tablero)
            print("Empate")
            jugando = False
        
        turno_actual = 1 - turno_actual # cambio de jugador

menu_principal()
