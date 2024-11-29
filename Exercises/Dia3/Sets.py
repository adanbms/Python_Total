#Tenemos distintas opciones para declarar un set, cualquiera funciona de la misma forma
mi_set = set([1,2,3,4,5])
print(type(mi_set)) #set
print(mi_set)
mi_set = set({1,2,3,4,5})
print(type(mi_set)) #set
print(mi_set)
mi_set = set((1,2,3,4,5))
print(type(mi_set)) #set
print(mi_set)
mi_set = {1,2,3,4,5}
print(type(mi_set)) #set
print(mi_set)

#Los elementod de los sets son unicos, aunque se agreguen valores repetidos, python los elimina
mi_set = set([1,1,1,1,1,1,2,3,3,4,5,"a",2.5,(1,2,3)])
print(mi_set) #El set elimina repetidos {1, 2, 3, 4, 5, 2.5, (1, 2, 3), 'a'}

#podemos saber su tamaño
print(len(mi_set))

#podemos validar si contiene un valor (al igual, que tupples, diccionarios(solo claves) y listas)
print(2 in mi_set)

#Union de sets
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3) # {1,2,3,4,5}

#Agregamso elementos
s3.add(6) #Agregara el 6
print(s3)
s3.add(2) #No sufrira cambios ya que el elemento ya existe
print(s3)

#Quitamos elementos del set
s3.remove(6) #Eliminara el 6
print(s3)
s3.remove(6) #Al no existir el elemento, nos dara un error
print(s3)
s3.discard(6) #Busca eliminar el 6 pero al no existir no se modifica el set, este metodo no devuelve error
print(s3)

sorteo = s3.pop() #Elimina un elemento aleatorio
print(sorteo)

s3.clear() #Vacia el set por completo
print(s3)