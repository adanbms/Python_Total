lista = ["a","b","c"]
indice = 0

#En este caso podemos acceder a los indices y alk contenido en la posicion de la lista por medio de la variable indice
for item in lista:
    print(indice, item)
    indice += 1

#sin embargo no es la mejor forma, aqui podriamos utilizasr enumerate
for item in enumerate(lista):
    print(item)#Obtendremos tuples del tipo (1, a)(2,b)(3,c)

for indice,item in enumerate(lista):
    print(indice, item)#Obtendremos el valor y el indice separados en variables

#Podemos convertir una lista en tuples utilizando enumerate
lista = list(enumerate(lista))
print(lista)#[(0, 'a'), (1, 'b'), (2, 'c')]