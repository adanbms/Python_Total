def suma(**kwargs):
    total=0
    for key,value in kwargs.items():
        print(f"{key} = {value}")
        total += value
    return total

print(suma(x=3, y=5, z=2)) #no es necesario enviarles diccionarios bien definidos, con tener key=value se tomaran como diccionarios

#Las funciones que utilizan argumentos indefinidos, tambi[en pueden utilizar definidos e incluso kwargs
#Para ello debemos organizarlos de la siguiente manera:
#1- Argumentos definidos
#2- *args
#3- *kwargs
def prueba(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for key,value in kwargs.items():
        print(f"{key} = {value}")

args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos'}

prueba(10,50,*args, **kwargs)