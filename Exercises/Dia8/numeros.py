def generadores(type):
    def perfumeria():
        n = 0
        while True:
            n += 1
            yield 'P-'+str(n)

    def farmacia():
        n = 0
        while True:
            n += 1
            yield 'F-'+str(n)

    def cosmeticos():
        n = 0
        while True:
            n += 1
            yield 'C-'+str(n)

    if type == 'cos':
        return cosmeticos()
    elif type == 'perf':
        return perfumeria()
    elif type == 'far':
        return farmacia()

def decorador(funcion):
    def otra_funcion(gen):
        print('Su turno es el siguiente: ')
        funcion(gen)
        print('Por fsvor espere...')
    return otra_funcion

def siguente_turno(gen):
    print(next(gen))