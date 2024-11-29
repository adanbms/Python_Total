#Funciones que implementan estructuras de control para realizar operaciones más complejas.
def chequear_3_cifras(lista):
    '''Valida si existen numeros de 3 cifras en una lista y los retorna en otra'''
    lista_3_cifras=[]
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras([1200,650,480,52])
print(resultado)