mi_tuple = (1,2,3,4) #definimos con parentesis
print(type(mi_tuple)) #tuple
print(mi_tuple)

#Puede definirse sin parentesis y con varios tipos de dato
mi_tuple = 1,"a",3.2,"Hola"
print(mi_tuple)
print(mi_tuple[0]) #Imprimimoe el valor en posición 0 -> 1
print(mi_tuple[1]) #Imprimimoe el valor en posición 1 -> a
print(mi_tuple[-2]) #Imprimimoe el valor en posición -2 -> 3.2

mi_tuple = (1,2,(10,20),3,1,4)
print(mi_tuple[2][0]) #Accedemos a 10

mi_tuple = list(mi_tuple) #Convertimos a lista
print(type(mi_tuple)) #list

#Asignamos valores a variables
#Asigna un elemento a cada variable siempre y cuando tengamos el mismo numero de valores que de variables (tambien funciona en listas)
t = 1,2,3,1
w,x,y,z = t
print(w,x,y,z)

print(len(t)) #Tamaño de mi tuple
print(t.count(1)) #Cuenat la cantidad de apariciones de un valor dentro del tuple
print(t.index(2)) #Devuelve el valor de posición del número 2 dentro del tuple

