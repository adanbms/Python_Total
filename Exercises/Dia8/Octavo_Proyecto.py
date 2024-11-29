'''
TURNERO DE FAMRACIA
'''

import numeros
from os import system

from Exercises.Dia8.numeros import siguente_turno


def inicio():
    gen_farmacia = numeros.generadores('far')
    gen_cosmeticos = numeros.generadores('cos')
    gen_perfumeria = numeros.generadores('perf')
    turno_decorado = numeros.decorador(siguente_turno)
    option = ''
    while option!='4':
        system('cls')
        option = input(f'''
    ------ FARMAMEX ------
    Bienvenido!
    ¿Para que area deseas un turno?

    1. Farmacia
    2. Cosmeticos
    3. Perfumeria
    4. Salir

    ingresa el numero de la opción que deseas: ''')
        match option:
            case '1':
                turno_decorado(gen_farmacia)
            case '2':
                turno_decorado(gen_cosmeticos)
            case '3':
                turno_decorado(gen_perfumeria)
            case '4':
                print('Saliendo del programa...')
            case _:
                print('Opción invalida, intenta de nuevo')

        input('Oprime ENTER para continuar.')

inicio()