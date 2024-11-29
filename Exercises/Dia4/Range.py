#RANGE
#Esta función no acepta floats en sus parametros
for numero in range(5): #Rango del 0 al 4
    print(numero)

for numero in range(1,5): #Rango del 1 al 5
    print(numero)

for numero in range(20,31): #Rango del 20 al 30
    print(numero)

for numero in range(20,31,3): #Rango del 20 al 30, de 3 en 3
    print(numero) #Es decir, 20, 23, 26 y 29

#También no puede servir para generar datos o listas a partir de un rango
lista = list(range(1,101)) #creamos una lista del 1 al 100