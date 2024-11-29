def mi_generador():
    '''Definimos 3 valores por generar con yield'''
    x=1
    yield x
    x+=1
    yield x
    x+=1
    yield x

g = mi_generador()

#Accedemos y generamos el primer valor
print(next(g))
#Accedemos y generamos el segundo valor
print(next(g))
#Accedemos y generamos el tercer valor
print(next(g))