import numpy as np
from numpy.random.mtrand import random
#from clases_flota import Tablero

barcos = {
    # nombre del barco : numero de sloras. 
    'barco_1':1,
    'barco_2':1, 
    'barco_3':1,
    'barco_4':1,
    'barco_5':2,
    'barco_6':2,
    'barco_7':2,
    'barco_8':3,
    'barco_9':3,
    'barco_10':4
    }

tablero_oculto = np.full ((10,10),' ')
tablero_oculto[9,9] = 'O'
tablero_oculto[5,5] = 'O'
tablero_oculto[0,7] = 'O'
tablero_oculto[0,5] = 'O'
tablero_oculto[1:3,2] = 'O'
tablero_oculto[5:7,2] = 'O'
tablero_oculto[3:5,4] = 'O'
tablero_oculto[6:9,4] = 'O'
tablero_oculto[1:4,9] = 'O'
tablero_oculto[9,4:8] = 'O'

def Menu():
    print("""
    ****************
    HUNDIR LA FLOTA
    ****************
    N) NUEVO JUEGO
    E) SALIR DEL JUEGO
    """)
    tecla = input("Elige una opción: ")
    if tecla == 'n' or 'N':
        NewGame()
    else:
        breakpoint

def NewGame():
    user = input("Introduce tu nombre: ")
    tablero = np.full ((10,10),' ')
    posicionar_barcos(tablero)
    tablero_pc = np.full ((10,10),' ')
    contador = 0
    contador_pc = 0
    Play(user,tablero, tablero_pc, contador, contador_pc)

def Play(user,tablero, tablero_pc, contador, contador_pc):
    mostrar_tablero(user,tablero, tablero_pc)
    batalla_ataque(tablero_pc, contador)
    batalla_defensa(tablero, contador_pc)
    if contador == 100:
        print("""
        ****************************
        ¡ENHORABUENA!¡FLOTA HUNDIDA!
        ****************************
        """)
    elif contador_pc == 100:
        print("""
        ****************************
        ¡UY!¡TU FLOTA SE HA HUNDIDO!
        ****************************
        """)
    else:
        Play(user,tablero, tablero_pc, contador, contador_pc)

def posicionar_barcos(tablero):
    print('''
    ****************
    PREPARA TU FLOTA
    ****************
    ''')
    for barco,sloras in barcos.items():
        print(f"Coloca tu {barco} con {sloras} sloras")
        x = int(input("Introduce coordenada x (horizontal): "))
        y = int(input("y ahora coordenada y (vertical): "))
        if sloras == 1:
            tablero[y,x] = 'O'
            print(tablero)    
        else:
            print("""¡Genial! Este barco tiene varias esloras:
            V) Vertical
            H) Horizontal
            """)
            timon = input("Elige una opción: ")
            if timon == 'V' or timon == 'v':
                z = y + sloras
                tablero[y:z,x] = 'O'
                print(tablero)
            elif timon == 'H' or timon =='h': 
                z = x + sloras
                tablero[y,x:z] = 'O'
                print(tablero)
            else:
                print('¡Valor no válido!')
    return tablero

def mostrar_tablero(user,tablero,tablero_pc):
    print(f"""

    * * * * * Tablero de {user} * * * * *

    """)
    print(tablero)

    print(f"""

    * * * * * Tablero máquina * * * * *
    
    """)
    print(tablero_pc)

def batalla_ataque(tablero_pc,contador):
    print('''
    ****************
    ATACA LA FLOTA
    ****************
    ''')
    while True == True:
        print("Introduce las cordenadas y dispara")
        x = int(input("Introduce coordenada x (horizontal): "))
        y = int(input("y ahora coordenada y (vertical): "))
        if tablero_oculto[y,x] == 'O':
            print('¡Tocado!')
            tablero_pc[y,x] = 'X'
            contador += 5
        else:
            tablero_pc[y,x] = '-'
            print('¡Agua!')
            return tablero_pc, contador

def batalla_defensa(tablero, contador_pc):
    while True == True:
        x = np.random.randint(0,10)
        y = np.random.randint(0,10)
        if tablero[y,x] == 'O':
           tablero[y,x] = 'X'
           contador_pc += 5
        else:
            tablero[y,x] = '-'
            return tablero, contador_pc

Menu()