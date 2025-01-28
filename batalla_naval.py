import time
import os

def mostrar_matriz(matriz_ver):
    for i in range(tamaño_tablero):
        col.append("{}".format(i+1))
    print(f"     {'      '.join(col[:tamaño_tablero])}") # .join para unir cadenas con el caracter que se le indique y [: tamaño_tablero] toma los últimos numeros que se le indique
    for i in range(tamaño_tablero):
        print(f"{i+1}", matriz_ver[i])
        print("\n")
# Validar la posición del barco antes de pintarlo en la matriz (Si cabe o no en los ejes (x, y))
def validar_tamaño_tablero(msg):
    while True:
        a = input(msg) # AQUI RECONOCE PRIMERO STR
        print(a)
        if a.isnumeric():
            w = int(a)
            while w < 5:
                a = input("Tamaño mínimo del tablero 5x5. Digite un valor mayor a 5: ")
                if a.isnumeric():
                    w = int(a)
                    if w >= 5:
                        break
                else:
                    print("Ingrese un valor numérico")
            break
        else:
            print("Ingrese un valor numérico")
    return int(a)

def coordenadas(tamaño_tablero):
    while True:
        x = int(input('     Digite  la posicion inicial x: '))-1
        y = int(input('     Digite  la posicion inicial y: '))-1 # Se resta uno por el indice de la lista
        if 0 <= x <= (tamaño_tablero-1) and 0 <= y <= (tamaño_tablero-1):
            print()
            break
        else:
            print('Posición fuera de rango')
    return x, y
def validar_ocupado_izq_der(pos_x,pos_y,tamaño_del_barco, matriz_jugador,flag_derecha,flag_izquierda):
    if  tamaño_del_barco<=(tamaño_tablero-(pos_x)):
        for i in range(tamaño_del_barco):

            if (matriz_jugador[pos_y][pos_x+i] == ['2'] or matriz_jugador[pos_y][pos_x+i] == ['3'] or matriz_jugador[pos_y][pos_x+i] == ['4'] or matriz_jugador[pos_y][pos_x+i] == ['5']):
                flag_derecha, flag_izquierda = False, False
                break
            elif(i == (tamaño_del_barco - 1)):
                flag_derecha, flag_izquierda = True, False
                print("      El barco solo cabe hacia la derecha")
    if pos_x+1 >= tamaño_del_barco:
        for j in range(tamaño_del_barco):
            if (matriz_jugador[pos_y][pos_x - j] == ['2'] or matriz_jugador[pos_y][pos_x - j] == ['3'] or matriz_jugador[pos_y][pos_x - j] == ['4'] or matriz_jugador[pos_y][pos_x - j] == ['5']):
                flag_izquierda, flag_derecha = False, False
                break
            elif(j == (tamaño_del_barco - 1)):
                flag_izquierda, flag_derecha= True, False
                print("      El barco solo cabe hacia la izquierda")

    return flag_derecha,flag_izquierda

def validar_ocupado_ar_ab(pos_x, pos_y, tamaño_del_barco, matriz_jugador, flag_arriba, flag_abajo):
    if tamaño_del_barco<=(tamaño_tablero-(pos_y)):
        for i in range(tamaño_del_barco):
            if (matriz_jugador[pos_y+i][pos_x] == ['2'] or matriz_jugador[pos_y+i][pos_x] == ['3'] or matriz_jugador[pos_y+i][pos_x] == ['4'] or matriz_jugador[pos_y+i][pos_x] == ['5']):
                flag_abajo, flag_arriba = False, False
                break

            elif i == (tamaño_del_barco - 1):
                flag_abajo, flag_arriba = True, False
                print("      El barco solo cabe hacia abajo")

    if (pos_y + 1) >= tamaño_del_barco:
        for j in range(tamaño_del_barco):
            if (matriz_jugador[pos_y - j][pos_x] == ['2'] or matriz_jugador[pos_y - j][pos_x] == ['3'] or matriz_jugador[pos_y - j][pos_x] == ['4'] or matriz_jugador[pos_y - j][pos_x] == ['5']):
                flag_arriba, flag_arriba = False, False
                break
            elif (j == (tamaño_del_barco - 1)):
                flag_arriba, flag_abajo = True, False
                print("      El barco solo cabe hacia arriba")

    return flag_arriba, flag_abajo

def validar_ubicacion( tamaño_del_barco, matriz_jugador):
    # while True:
    #     pos_x = int(input('     Digite  la posicion inicial x: '))-1
    #     pos_y = int(input('     Digite  la posicion inicial y: '))-1 # Se resta uno por el indice de la lista
    #     if pos_x > tamaño_tablero or pos_y > tamaño_tablero:
    #         print('Posición fuera de rango')
    #     else:
    #         break
    pos_x,pos_y=coordenadas(tamaño_tablero)
    tamaño_del_barco = int(tamaño_del_barco)
    time.sleep(200/1000)
    print()
    print('|--------------------------------------------------|')
    print('|        Validación de la posición del barco       |')
    print('|--------------------------------------------------|')
    print()
    time.sleep(200/1000)
    Validacion_ok=False
    # Flags = validar la dirección
    while Validacion_ok == False:
        flag_arriba, flag_abajo, flag_izquierda, flag_derecha = True, True, True, True

        if (tamaño_del_barco<=(tamaño_tablero-(pos_x))) and (pos_x + 1 >= tamaño_del_barco) and (flag_derecha == True) and (flag_izquierda == True):
            for i in range(tamaño_del_barco):

                if (matriz_jugador[pos_y][pos_x+i] == ['2'] or matriz_jugador[pos_y][pos_x+i] == ['3'] or matriz_jugador[pos_y][pos_x+i] == ['4'] or matriz_jugador[pos_y][pos_x+i] == ['5'] ) or  (matriz_jugador[pos_y][pos_x - i] == ['2'] or matriz_jugador[pos_y][pos_x - i] == ['3'] or matriz_jugador[pos_y][pos_x - i] == ['4'] or matriz_jugador[pos_y][pos_x - i] == ['5'] ):
                    flag_izquierda, flag_derecha = False,False
                    flag_derecha,flag_izquierda= validar_ocupado_izq_der(pos_x,pos_y,tamaño_del_barco, matriz_jugador,flag_derecha,flag_izquierda)
                    break
                elif (i == (tamaño_del_barco - 1)) :
                    print("      El barco si cabe en X (izquierda y derecha)")
                    flag_izquierda,flag_derecha = True,True

        else:
            flag_derecha,flag_izquierda = validar_ocupado_izq_der(pos_x,pos_y,tamaño_del_barco, matriz_jugador,flag_derecha,flag_izquierda)

        if tamaño_del_barco<=(tamaño_tablero-(pos_y)) and (pos_y + 1) >= tamaño_del_barco and (flag_arriba == True) and (flag_abajo == True):
            for i in range(tamaño_del_barco):
                if (matriz_jugador[pos_y+1][pos_x] == ['2'] or matriz_jugador[pos_y+1][pos_x] == ['3'] or matriz_jugador[pos_y+1][pos_x] == ['4'] or matriz_jugador[pos_y+1][pos_x] == ['5'] ) or  (matriz_jugador[pos_y - i][pos_x] == ['2'] or matriz_jugador[pos_y - i][pos_x] == ['3'] or matriz_jugador[pos_y - i][pos_x] == ['4'] or matriz_jugador[pos_y - i][pos_x] == ['5'] ):
                    flag_arriba,flag_abajo = validar_ocupado_ar_ab(pos_x, pos_y, tamaño_del_barco, matriz_jugador, flag_arriba, flag_abajo)
                    break
                elif (i == (tamaño_del_barco - 1)) :
                    print("      El barco si cabe en Y (arriba y abajo)")
                    flag_arriba,flag_abajo = True, True
        else:
            flag_arriba,flag_abajo = validar_ocupado_ar_ab(pos_x, pos_y, tamaño_del_barco, matriz_jugador, flag_arriba, flag_abajo)

        if (matriz_jugador[pos_y][pos_x] == ['2'] or matriz_jugador[pos_y][pos_x] == ['3'] or matriz_jugador[pos_y][pos_x] == ['4'] or matriz_jugador[pos_y][pos_x] == ['5']) or (flag_arriba== False and flag_abajo == False and flag_izquierda == False and flag_derecha == False):
            print(" Posición ocupada")
            pos_x,pos_y = coordenadas(tamaño_tablero)
        else:
            Validacion_ok = True
            break

    return flag_abajo, flag_arriba, flag_izquierda, flag_derecha,pos_y,pos_x


#Selecciona el barco a utilizar

def seleccion_barcos():
    for j in range(len(jugadores)):
        cantidad_barcos = [1, 0, 0, 0]

        if jugadores[j] == 1:
            matriz_prueba = matriz_jugador1
        elif jugadores[j] == 2:
            matriz_prueba = matriz_jugador2 # /////Reasignar matriz////

        while cantidad_barcos != [0, 0, 0, 0]:
            time.sleep(200/1000)
            print()
            print('|--------------------------------------------------|')
            print(f'|              BARCOS JUGADOR {j+1}                    |')
            print('|--------------------------------------------------|')
            print(f'|     1. Fragata (2 posiciones)       ({cantidad_barcos[0]}und)       |')
            print(f'|     2. Submarino (3 posiciones)     ({cantidad_barcos[1]}und)       |')
            print(f'|     3. Porta Aviones (4 posiciones) ({cantidad_barcos[2]}und)       |')
            print(f'|     4. Crucero (5 posiciones)       ({cantidad_barcos[3]}und)       |')
            print('|--------------------------------------------------|')
            print()
            time.sleep(200/1000)
            opcion_barco = input('Escoja el barco a colocar: ')
            time.sleep(200/1000)


            while True:
                #se selecciona el barco y se resta la cantidad de barcos.
                if opcion_barco == '1' and cantidad_barcos[0] > 0:
                    opcion_barco = tamaño_barcos[0]
                    cantidad_barcos[0] -= 1
                elif opcion_barco == '2' and cantidad_barcos[1] > 0:
                    opcion_barco = tamaño_barcos[1]
                    cantidad_barcos[1] -= 1
                elif opcion_barco == '3' and cantidad_barcos[2] > 0:
                    opcion_barco = tamaño_barcos[2]
                    cantidad_barcos[2] -= 1
                elif opcion_barco == '4' and cantidad_barcos[3] > 0:
                    opcion_barco = tamaño_barcos[3]
                    cantidad_barcos[3] -= 1
                else:
                    print('     Digite una opción valida')
                    opcion_barco = input('Escoja el barco a colocar: ')
                    continue
                break
            prueba_matriz(opcion_barco, matriz_prueba, j + 1)


# Crear tablero

def crear_tablero():
    matriz = []
    for i in range(tamaño_tablero):
        fila = []
        for j in range(tamaño_tablero):
            fila.append(['_'])
        matriz.append(fila)
    return matriz

def prueba_matriz(tamaño_barco, matriz_prueba1, jugador):
    flags = validar_ubicacion(tamaño_barco, matriz_prueba1)
    pos_y = flags[4]
    pos_x = flags[5]
    #print(flags)
    if flags !=(False, False, False, False):
        time.sleep(200/1000)
        print()
        print('|--------------------------------------------------|')
        print('|                     DIRECCIÓN                    |')
        print('|--------------------------------------------------|')
        print('|     1. Derecha 2. Izquierda 3. Abajo 4. Arriba   |')
        print('|--------------------------------------------------|')
        print()
        time.sleep(200/1000)
        direccion = int(input('Elija la dirección para colocar el barco: '))
        time.sleep(200/1000)

        while True:
            if direccion == 1 and flags[3]:
                for i in range(0, tamaño_barco):
                    #matriz_prueba1[pos_y][pos_x + i] = ['&']
                    matriz_prueba1[pos_y][pos_x + i] = [f'{tamaño_barco}']
                break
            elif direccion == 2 and flags[2]:
                for i in range(0, tamaño_barco):
                    #matriz_prueba1[pos_y][pos_x - i] = ['&']
                    matriz_prueba1[pos_y][pos_x - i] = [f'{tamaño_barco}']
                break
            elif direccion == 3 and flags[0]:
                for i in range(0, tamaño_barco):
                    #matriz_prueba1[pos_y + i][pos_x] = ['&']
                    matriz_prueba1[pos_y + i][pos_x ] = [f'{tamaño_barco}']
                break
            elif direccion == 4 and flags[1]:
                for i in range(0, tamaño_barco):
                    #matriz_prueba1[pos_y - i][pos_x] = ['&']
                    matriz_prueba1[pos_y - i][pos_x] = [f'{tamaño_barco}']
                break
            else:
                print('     Digite una opción valida')
                direccion = int(input('Elija la dirección para colocar el barco: '))
        # mostrar_matriz(matriz_jugador1)
        # mostrar_matriz(matriz_jugador2)
        mostrar_matriz(matriz_prueba1)
        # mostrar_matriz(matriz_prueba2)

def lanzamientos(total_puntos):
    #fallo = 0
    Barco2j1, Barco3j1, Barco4j1, Barco5j1 = 0, 0, 0, 0
    Barco2j2, Barco3j2, Barco4j2, Barco5j2 = 0, 0, 0, 0
    j1_puntos=0
    j2_puntos=0
    while j1_puntos != total_puntos  or j2_puntos != total_puntos:
        i=1
        if i<=2:
            time.sleep(200/1000)
            print()
            print('|----------------------------------------------------------------------|')
            print(f'|                          TURNO JUGADOR {i}                             |')
            print('|----------------------------------------------------------------------|')
            time.sleep(200/1000)
            while i==1:
                matriz_prueba = lanzamientos_jugador1
                mostrar_matriz(matriz_prueba)
                pos_x,pos_y=coordenadas(tamaño_tablero)

                if lanzamientos_jugador1[pos_y][pos_x] == ["O"]:
                    print("Ya disparaste en ese lugar")
                if lanzamientos_jugador1[pos_y][pos_x] == ["X"]:
                    print("Ya disparaste en ese lugar")
                elif (matriz_jugador2[pos_y][pos_x] == ['2'] or matriz_jugador2[pos_y][pos_x] == ['3'] or matriz_jugador2[pos_y][pos_x] == ['4'] or matriz_jugador2[pos_y][pos_x] == ['5']):

                    lanzamientos_jugador1[pos_y][pos_x]=["X"]
                    print('|--------------------- DISPARO EXITOSO ✓ ---------------------|')
                    time.sleep(1)
                    if matriz_jugador2[pos_y][pos_x] == ['2']:
                        Barco2j1=Barco2j1+1
                        j1_puntos += 1
                        if Barco2j1 == 2:
                            print("--------- ¡Enhorabuena! Derribaste la Fragata enemiga ---------")
                            print()
                            time.sleep(800/1000)
                    elif matriz_jugador2[pos_y][pos_x] == ['3']:
                        Barco3j1=Barco3j1+1
                        j1_puntos += 1
                        if Barco3j1 == 3:

                            print("---------¡Enhorabuena! Derribaste el Submarino enemigo --------")
                            print()
                            time.sleep(800/1000)
                    elif matriz_jugador2[pos_y][pos_x] == ['4']:
                        Barco4j1=Barco4j1+1
                        j1_puntos += 1
                        if Barco4j1 == 4:

                            print("------ ¡Enhorabuena! Derribaste el Porta Aviones enemigo ------")
                            print()
                            time.sleep(800/1000)
                    elif matriz_jugador2[pos_y][pos_x] == ['5']:
                        Barco5j1=Barco5j1+1
                        j1_puntos += 1
                        if Barco4j1 == 5:

                            print("--------- ¡Enhorabuena! Derribaste el Crucero enemigo ---------")
                            print()
                            time.sleep(800/1000)

                    if total_puntos == j1_puntos:
                        print('|-----------------------------------------------------------------------------------------|')
                        time.sleep(200/1000)
                        print('|                            E L   J U G A D O R    #  1                                  |')
                        time.sleep(200/1000)
                        print('|                                        E S   E L  G A N A D O R                         |')
                        time.sleep(200/1000)
                        print('|-----------------------------------------------------------------------------------------|')
                        time.sleep(800/1000)
                        break
                    print("---------------------- Dispare nuevamente ---------------------")

                else:
                    lanzamientos_jugador1[pos_y][pos_x]=["O"]
                    mostrar_matriz(matriz_prueba)
                    print('|--------------------- DISPARO FALLIDO X ---------------------|')
                    time.sleep(800/1000)
                    i=2
                    break
            if j1_puntos == total_puntos:
                break
            if j2_puntos == total_puntos:
                break
            while i==2:
                print()
                print('|----------------------------------------------------------------------|')
                print(f'|                          TURNO JUGADOR {i}                             |')
                print('|----------------------------------------------------------------------|')
                matriz_prueba = lanzamientos_jugador2
                mostrar_matriz(matriz_prueba)
                pos_x,pos_y=coordenadas(tamaño_tablero)


                if lanzamientos_jugador2[pos_y][pos_x] == ["O"]:
                    print("Ya disparaste en ese lugar")
                if lanzamientos_jugador2[pos_y][pos_x] == ["X"]:
                    print("Ya disparaste en ese lugar")
                elif (matriz_jugador1[pos_y][pos_x] == ['2'] or matriz_jugador1[pos_y][pos_x] == ['3'] or matriz_jugador1[pos_y][pos_x] == ['4'] or matriz_jugador1[pos_y][pos_x] == ['5']):

                    lanzamientos_jugador2[pos_y][pos_x]=["X"]
                    print('|--------------------- DISPARO EXITOSO ✓ ---------------------|')
                    time.sleep(1)

                    if matriz_jugador1[pos_y][pos_x] == ['2'] :
                        Barco2j2=Barco2j2+1
                        j2_puntos+=1
                        if Barco2j2 == 2:
                            print("--------- ¡Enhorabuena! Derribaste la Fragata enemiga ---------")
                            print()
                            time.sleep(800/1000)
                    elif matriz_jugador1[pos_y][pos_x] == ['3']:
                        Barco3j2=Barco3j2+1
                        j2_puntos+=1
                        if Barco3j2 == 3:
                            print("---------¡Enhorabuena! Derribaste el Submarino enemigo --------")
                            print()
                            time.sleep(800/1000)
                    elif matriz_jugador1[pos_y][pos_x] == ['4']:
                        Barco4j2=Barco4j2+1
                        j2_puntos+=1
                        if Barco4j2 == 4:
                            print("------ ¡Enhorabuena! Derribaste el Porta Aviones enemigo ------")
                            print()
                            time.sleep(800/1000)
                    elif matriz_jugador1[pos_y][pos_x] == ['5']:
                        Barco5j2=Barco5j2+1
                        j2_puntos+=1
                        if Barco4j2 == 5:
                            print("--------- ¡Enhorabuena! Derribaste el Crucero enemigo ---------")
                            print()
                            time.sleep(800/1000)

                    if total_puntos==j2_puntos:
                        print('|-----------------------------------------------------------------------------------------|')
                        time.sleep(200/1000)
                        print('|                            E L   J U G A D O R    #  2                                  |')
                        time.sleep(200/1000)
                        print('|                                        E S   E L  G A N A D O R                         |')
                        time.sleep(200/1000)
                        print('|-----------------------------------------------------------------------------------------|')
                        time.sleep(800/1000)
                        break
                    time.sleep(800/1000)
                    print("---------------------- Dispare nuevamente ---------------------")

                else:
                    lanzamientos_jugador2[pos_y][pos_x]=["O"]
                    mostrar_matriz(matriz_prueba)
                    print('|--------------------- DISPARO FALLIDO X ---------------------|')
                    time.sleep(800/1000)
                    i=1
                    break
            if j1_puntos == total_puntos:
                break
            if j2_puntos == total_puntos:
                break


col = []
Validacion_ok = False
#barcos = ["Fragata", "Crucero", "Portaaviones", "Submarino", "Destructor"]
#direccion = {'arriba': -1, 'abajo': 1, 'izquier1da': -1, 'derecha': 1}
tamaño_barcos=[2, 3, 4, 5]
cantidad_barcos = [1, 03

                   , 0, 0]
total_puntos = ((tamaño_barcos[0] * cantidad_barcos[0])+(tamaño_barcos[1] * cantidad_barcos[1])+(tamaño_barcos[2] * cantidad_barcos[2])+(tamaño_barcos[3] * cantidad_barcos[3]))
jugadores=[1,2]
print('|----------------------------------------------------------------------|')
time.sleep(200/1000)
print('| B I E N V E N I D O    A   B A T A L L A  N A V A L                  |')
time.sleep(200/1000)
print('| E N    P Y T H O N                                                   |')
time.sleep(200/1000)
print('|----------------------------------------------------------------------|')
time.sleep(200/1000)
print('| INSTRUCCIONES DEL JUEGO                                              |')
time.sleep(200/1000)
print('| - Batalla naval se juega con 2 jugadores                             |')
time.sleep(200/1000)
print('| - Se debe escoger un tamaño para el tablero:                         |')
time.sleep(200/1000)
print('|                   Tamaño mínimo del tablero: 5x5                     |')
time.sleep(200/1000)
print('|                   Tamaño óptimo: 10x10                               |')
time.sleep(200/1000)
print('| - Cada jugador escogerá 5 barcos para colocar en su tablero          |')
time.sleep(200/1000)
print('| - El primero en derribar los barcos del oponente gana                |')
time.sleep(200/1000)
print('|----------------------------------------------------------------------|')
#time.sleep(10)
print('|                            ¡Buena suerte!                            |')
print('|----------------------------------------------------------------------|')
print()
tamaño_tablero = validar_tamaño_tablero('|--------------------Digite el tamaño del tablero:-------------------|\n -> ')
#Solicita al usuario el tamaño del tablero
matriz_vista = crear_tablero()
time.sleep(200/1000)
print('|----------------------------------------------------------------------|')
print('|                          TAMAÑO DEL TABLERO                          |')
print('|----------------------------------------------------------------------|')
time.sleep(200/1000)
mostrar_matriz(matriz_vista)
# Crear matrices para cada jugador

matriz_jugador1 = crear_tablero()
lanzamientos_jugador1 = crear_tablero()
matriz_jugador2 = crear_tablero()
lanzamientos_jugador2 = crear_tablero()

# Iniciar la selección de barcos
seleccion_barcos()
time.sleep(3)
os.system('cls')
time.sleep(500/1000)
print('|----------------------------------------------------------------------|')
time.sleep(500/1000)
print('|              ¡ Q U E   C O M I E N C E  E L  J U E G O !             |')
time.sleep(500/1000)
print('|----------------------------------------------------------------------|')
time.sleep(1)
lanzamientos(total_puntos)
time.sleep(1)
os.system('cls')

time.sleep(500/1000)
print(' F')
time.sleep(500/1000)
print('         I')
time.sleep(500/1000)
print('                 N')
time.sleep(500/1000)
print('                             D')
time.sleep(500/1000)
print('                                     E')
time.sleep(500/1000)
print('                                             L')
time.sleep(500/1000)
print('                                                         J')
time.sleep(500/1000)
print('                                                                 U')
time.sleep(500/1000)
print('                                                                         E')
time.sleep(500/1000)
print('                                                                                 G')
time.sleep(500/1000)
print('                                                                                         O')
time.sleep(500/1000)
print('                                                                          ')
time.sleep(200/1000)
print('                                                       |                  ')
time.sleep(200/1000)
print('                                       ------          |                  ')
time.sleep(200/1000)
print('                                                       |                  ')
time.sleep(200/1000)
print('                                                                          ')
time.sleep(200/1000)
print('                                                                          ')
time.sleep(200/1000)
print('                                        --              --                ')
time.sleep(200/1000)
print('                                          --          --                  ')
time.sleep(200/1000)
print('                                            ----------                    ')
time.sleep(200/1000)
print('                                                                          ')
time.sleep(200/1000)
print('                               g r a c i a s   p o r   j u g a r !        ')
time.sleep(200/1000)
