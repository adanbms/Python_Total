#Se utiliza para devolver un resultado cuando estamos utilizando funciones. Para utilizarlo debemos poner la palabra return seguido del dato que deseamos retornar a donde la función fue llamada.
def multiplicar(num1, num2):
    '''Función que multiplica 2 numeros y retorna el resultado'''
    return num1 * num2


resultado = multiplicar(5, 10)  # Multiplica 5 x 10 y almacena el resultado
print(resultado)  # debe ser 50


# Podemos utilizar variables internas para manejar los datos
# es buena practica y la función sigue teniendo el mismo comportamiento
def multiplicar_v2(num1, num2):
    '''Función que multiplica 2 numeros y retorna el resultado'''
    res = num1 * num2
    return res


resultado = multiplicar_v2(5, 10)  # Multiplica 5 x 10 y almacena el resultado
print(resultado)  # debe ser 50