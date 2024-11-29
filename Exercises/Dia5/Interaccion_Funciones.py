from random import shuffle

#Crear lista inicial de palitos
palitos = ['-','--','---','----']

#Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#Pedir intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input(f'Elige un número del 1 al 4: ')
    return int(intento)

#Comprobar Intento
def checar_intento(lista, intento):
    if lista[intento-1] == '=':
        print('A lavar los platos')
    else:
        print('Esta vez te has salvado')

    print(f'Te ha tocado {lista[intento-1]}')


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
checar_intento(palitos_mezclados,seleccion)