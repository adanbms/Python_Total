mi_lista = ["a","b","c"]
#index       |   |   |
#index       0   1   2

print(type(mi_lista)) #Tipo de dato: list

#Obtener longitud o tamaño
print(len(mi_lista)) #En este caso nos da el numero de elementos que contiene
#Obtener elementos
print(mi_lista[0]) #obtiene el valor "a"
#Obtener subconjuntos o fraccionar lista
print(mi_lista[0:2]) #obtiene ['a', 'b'] ya que, aunque "c" esta en la posición 2, no se incluye en el limite

#Haciendo listas de diferentes tipos de dato
otra_lista = ["hola", 55, 6.1]


#Concatenando listas
print(mi_lista+otra_lista) #Podemos añadir otra lista -> ['a', 'b', 'c', 'hola', 55, 6.1]
print(mi_lista*3) #Podemos multiplicar los elementos de la lista -> ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

mi_lista3 = mi_lista+otra_lista
mi_lista3[0] = 'alfa'
print(mi_lista3) #Cambiamos el primer elemento de la lista por la cadena "alfa"

#agregando elementos
mi_lista3.append("g") #Esta linea agrega el elemento "g" al final de la lista
print(mi_lista3)

#eliminando elementos
mi_lista3.pop() #Elimina el ultimo elemento de la lista
mi_lista3.pop(0) #Elimina el elemento en la posición dada de la lista

#podemos utilizar una variable para guardar el elemento popeado
popped = mi_lista3.pop()
print(popped)

#Podemos ordenar una lista utilizando sort
lista = ['d','r','a','b','h']
print(lista)
lista.sort() #En este caso sort no retorna una nueva lista sino que ordena la original y guarda el resultado en la misma
print(lista)
#por lo que si asignamos esto a una variable obtendremos un NoneType que es el tipo de dado de los obetos que no tienen valor
lista.reverse()
print(lista) #Aqui utilizamos reverse para ordenar inversamente

