def suma (num1, num2):
    return num1 + num2

print(suma(10,23)) #Imprimira la suma de los 2 numeros
''' Si enviamos:
    print(suma(10,23,33)) 
    Nos dara un error ya que la función solo tiene definidos 2 argumentos y estamos pasando 3 '''

#cuando esto pasa podemos utilizar los argumentos indefinidos de Python de la siguiente forma
def suma_args(*args):
    result=0
    for arg in args:
        result+=arg
    return result

#Utilizando esto no importa cuantos argumentos tengamos simepre podremos hace la suma
print(suma_args(10,23,33,33455,653,21))
print(suma_args(10,21))
print(suma_args(10,23,33,))