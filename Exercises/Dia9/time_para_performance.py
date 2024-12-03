'''
Podemos medir el tiempo de ejecución de un programa utilizando el módulo time
estableciendo un tiempo de inicio, un tiempo de finalización y obteniendo la diferencia entre estos 2

Aunque a veces el tiempo es muy pequeño y no es posible medirlo con esta clase
'''
import time
import timeit

#Definimos 2 métodos que solucionan el mismo problema
def prueba_for(num):
    list = []
    for n in range(1, num+1):
        list.append(n)
    return list

def prueba_while(num):
    list = []
    contador = 1
    while contador <= num:
        list.append(contador)
        contador += 1
    return list

#Medimos sus tiempos con time
inicio = time.time()
prueba_for(10)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(10)
final = time.time()
print(final - inicio)

'''
Sin embargo, si se trata de performance de funciones, en python tenemos la opción de utilizar
el módulo timeit para simular la ejecución de un método n cantidad de veces y obtener 
el tiempo de ejecución exacto

Esto es útil cuando tenemos distintas soluciones a un mismo problema y no sabemos cual es la más eficiente
en estos casos podemos utilizar timeit para resolver este problema.
'''
#Definimos un statement y un setup para la primer función (llamado y definiciópn de función)
stmt = '''
prueba_for(10)
'''

setup = '''
def prueba_for(num):
    list = []
    for n in range(1, num+1):
        list.append(n)
    return list
'''
#Enviamos stmt, setup y la cantidad de veces que se repetira la ejecución para la evaluación
tiempo = timeit.timeit(stmt,setup,number=1000000)
print(f'prueba_for: {tiempo}')
#REPETIMOS PROCESO PARA FUNCIóN 2
stmt = '''
prueba_while(10)
'''

setup = '''
def prueba_while(num):
    list = []
    contador = 1
    while contador <= num:
        list.append(contador)
        contador += 1
    return list
'''
#Enviamos stmt, setup y la cantidad de veces que se repetira la ejecución para la evaluación
tiempo = timeit.timeit(stmt,setup,number=1000000)
print(f'prueba_while: {tiempo}')