#Juego de Ahorcado
#Importar choice para seleccionar una palabra de una lista
from random import choice
from random import randint

lista_palabras = ['BELEN', 'NACIMIENTO', 'PESEBRE', 'PORTAL', 'ARBOL', 'ANGELITO', 'DIABLITO', 'PASTOR', 'ESTRELLA', 'MAGOS']
vidas = 6

def seleccionar_palabra():
    palabra = choice(lista_palabras)
    palabra = list(l for l in palabra)
    return palabra

def ocultar_palabra(palabra):
    pista = list('-'*len(palabra))
    num = randint(0,len(palabra))
    pista[num] = palabra[num]
    return pista

def lista_a_palabra(lista):
    palabra = "".join(lista)
    return palabra

#Pedir y validar letra
def pedir_letra():
    letra = ''
    es_letra = False
    while not es_letra:
        letra = input(f'Vida:{vidas} -- ¿Que letra crees que complete la palabra?: ').upper()
        if len(letra) == 1 and letra in 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ':
            es_letra = True
        else:
            print('No ingresaste una letra')
            es_letra = False
    return letra

#Validar que sea una letra de la palabra
def letra_en_palabra(letra, palabra):
    if letra in palabra:
        return True
    else:
        return False

def descubrir_letras(letra, palabra, palabra_oculta):
    index = 0
    for l in palabra:
        if l == letra:
            palabra_oculta[index] = palabra[index]
        index += 1
    return palabra_oculta

#Validar si ha adivinado
def ha_adivinado(p, p_guion):
    if p == p_guion:
        return True
    else:
        return False

#Funciones y luego el código que la implementa
palabra_secreta = seleccionar_palabra()
palabra_guiones = ocultar_palabra(palabra_secreta)
letras_incorrectas = []
print(f'--#---------------- Bienvenido al ahorcado navideño ---------------#--\n--#-- Tienes {vidas} vidas para adivinar la palabra ¿Estás listo? --#--\n\tTu palabara es: {lista_a_palabra(palabra_guiones)}')

while vidas > 0:
    if ha_adivinado(palabra_secreta, palabra_guiones):
        print('------------------------------------------------------------------------------')
        print(f'\tFelicidades!!! Has adivinado, el juego ha terminado. te sobraron {vidas} vidas')
        print(f'\tTu palabra era {lista_a_palabra(palabra_secreta)}')
        break
    else:
        letra = pedir_letra()
        if letra_en_palabra(letra, palabra_secreta):
            palabra_guiones = descubrir_letras(letra,palabra_secreta,palabra_guiones)
            print(f"\tHas acertado, tu palabra es: {lista_a_palabra(palabra_guiones)}")
        else:
            vidas -= 1
            letras_incorrectas.append(letra)
            print(f"\tHas fallado, te quedan {vidas} vidas, intenta de nuevo. \n\tTu palabra es: {lista_a_palabra(palabra_guiones)}\n\t Letras incorrectas: {lista_a_palabra(letras_incorrectas)}")
else:
    print('------------------------------------------------------------------------------')
    print('\tEl juego ha rerminado, no has podido adivinar la palabra y no tienes más vidas')
    print(f'\tTu palabra era {lista_a_palabra(palabra_secreta)}')
    print('\tSuerte para la proxima!')
