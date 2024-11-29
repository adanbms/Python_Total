'''Esta función genera la lista completa en memoria ya lista para accede con todos los recursos que eso consuma'''
def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista

'''yeld solo reserva el espacio en memoria de un valor, pero no se utiliza hasta que se lo pidamos con next
una vez usando next YIELD recuerda el ultimo valor proveido y lleva un control para que la siguiente vez que hagamos next nos de el valor siguiente de la secuencia o lista'''
def mi_generador():
    for x in range(1,4):
        yield x * 10

print(mi_funcion()) #Imprime la lista completa
print(mi_generador()) #Imprime espacio en memoria <generator object mi_generador at 0x0000013DA7CF47D0>

g = mi_generador() #guardamos valor en una variable

print(next(g)) #Pedimos netx y yeld genera el primer valor accesible
print(next(g)) #Pedimos netx y yeld genera el segundo valor accesible
print(next(g)) #Pedimos netx y yeld genera el tercer valor accesible
print(next(g)) #Como no hay más valores dara un error StopIteration