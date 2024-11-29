#Definimos las funciones dentro de una función
def cambier_letras(tipo):
    def mayusculas(texto):
        print(texto.upper())

    def minusculas(texto):
        print(texto.lower())

    #Si enviamos may retornara mayusculas(), si es min entonces minusculas()
    if tipo == 'may':
        return mayusculas
    elif tipo == 'min':
        return minusculas

#Asignamos la función que retorne cambiar letras, en este caso mayusculas()
operacion = cambier_letras('may')
#operaciópn toma el comportamiento de mayusculas, por lo que si le pasamos texto hara su función
operacion('palabra')

def decorar_saludo(funcion):
    #esta función decorará cualquier función
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

#Podemos utilizarla como decorador simplemente agregando un @ antes de su nombre
#el paramtero sera la función que tenga debajo
@decorar_saludo
def may_dec(texto):
    print(texto.upper())

def mayus(texto):
    print(texto.upper())

def minus(texto):
    print(texto.lower())

#Llamar con decoro y etiqueta
may_dec('fede')

#LLamar con decoro pero sin etiqueta
mayuscula_decorada = decorar_saludo(mayus)
mayuscula_decorada('fede')

#Lamar sin decoro y sin etiqueta
mayuscula_decorada = mayus()
mayuscula_decorada('fede')