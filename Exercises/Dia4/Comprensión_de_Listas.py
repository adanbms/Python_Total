palabra = "python"
lista = []

for letra in palabra:
    lista.append(letra)

print(lista) #Definimos la lista ['p', 'y', 't', 'h', 'o', 'n']

#Otra forma de hacerlo es con compresión de listas
lista2 = [letra for letra in palabra] #Lista de una letra por cada letra que exista en palabra
print(lista2)

lista3 = [a for a in "thisword"] #lista ['t', 'h', 'i', 's', 'w', 'o', 'r', 'd']
print(lista3)

#UTILIZANDO NUMEROS
lista4 = [n for n in range(0,21,2)] #lista compuesta de cada numero par en el rango de 0 a 20
print(lista4) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

lista5 = [n/2 for n in range(0,40,4)] #lista de cada número multiplo de 4 del rango 0-39 dividido entre 2
print(lista5) #[0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0]

#AGREAGANDO UN IF
lista6 = [n for n in range(5,46,5) if n%2 == 0] #Agrega a la lista solo los numeros pares en el rango del 5 al 45, con intervalos de 5
print(lista6) #[10, 20, 30, 40]

#AGREAGANDO UN IF-ELSE
lista6 = [n if n%2 == 0 else 'impar' for n in range(5,46,5)] #Agrega a la lista solo los numeros pares en el rango del 5 al 45, con intervalos de 5
print(lista6) #['impar', 10, 'impar', 20, 'impar', 30, 'impar', 40, 'impar']

#EQUIVALENTES DE PIES A METROS
pies = [10,20,30,40,50]
metros = [p/3.281 for p in pies]
print(metros) #[3.047851264858275, 6.09570252971655, 9.143553794574824, 12.1914050594331, 15.239256324291373]