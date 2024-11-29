def suma():
    n1 = input('Ingresa el primer numero: ')
    n2 = input('Ingresa el segundo numero: ')
    print(n1+n2)
    print('Gracias por sumar!')

try:
    '''try Pone a prueba el código que contiene'''
    suma()
except TypeError:
    '''Podemos preparar el código para distintos tipos de errores y utilizar varios excepts'''
    print('Estas intentanco concatenar tipos distintos')
except ValueError:
    print('Ese no es un número')
else:
    '''Si todo sale bien y no falla se ejecutara else'''
    print('Todo salio bien, grascias por usar el programa..')
finally:
    '''Y si falla o no siempre se ejecutara el código dentro de finally'''
    print('Finalizando ejecución')