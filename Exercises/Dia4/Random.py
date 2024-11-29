from random import *

#RANDINT
aleatorio = randint(1,100) #Especificamos rango del número entero generado
print(aleatorio)

#UNIFORM
aleatorio = round(uniform(1,100), 2) #Especificamos rango del número decimal generado y decimales requeridos con random
print(aleatorio)

#RANDOM
aleatorio = random() #elige un número decimal entre 0 y 1
print(aleatorio)

#CHOICE
colores= ["azul", "rojo", "verde", "amarillo"]
aleatorio = choice(colores) #Elige un elemento aleatorio de una colección
print(aleatorio)

#SHUFLE
numeros = list(range(5,50,5)) #Lista del 5 al 50 con multiplos de 5 nadamas
shuffle(numeros) #Modifican la lista generada con un orden aleatorio cada que se ejcuta
print(numeros)