nombres = ['Fran','Belen','Carlos','Ana','Juan']
#Por cada elemento en nombres escribir 'Hola'
for nombre in nombres: #nombre es una variable que define cada elemento de la lista
    print("Hola "+ nombre)

print()
#podemos obtener más datos de los elementos durante la iteración, como por ejemplo el index
for nombre in nombres: #nombre es una variable que define cada elemento de la lista
    posicion = nombres.index(nombre) + 1 #Ponemos más 1 ya que la lista inicia el conteo en 0
    print(f"Hola {nombre} tienes la posición {posicion}")

print()
#Podemos incluir más estructuras dentro de este loop, por ejemplo IF
#Imprimir nombre solo SI CONTIENE LA LETRA L
for nombre in nombres:
    if nombre.upper().find("L") != -1:
        print("El nombre "+ nombre + " tiene la letra L")

print()

#Adicionando valores a una variable en cada asignación
numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor += numero
    print(mi_valor)

print()

#Loop que por cadas letrqa en palabra imprima letra
palabra = 'letra' #Los string son iterables por lo que no es necesario hacer conversiones para iterarlo
for letra in palabra: #Letra solo es el nombre de la variable no tiene que ser especifico
    print(letra)

print()

#Podemos iterar con tuples o listas
for num in (1,2,3): #Podemos definir el objeto a iterar en esta sentencia
    print(num)

print()

#Con listas dentro de listas
for num1,num2 in [[1,2],[3,4],[5,6]]: #por cada objeto en la lista se asigna a cada variable por cada iteración
    print(str(num1)+' '+str(num2))

print()

for list1 in [[1,2],[3,4],[5,6]]: #tambien podemos solo obtener el objeto
    print(list1)

print()

#También podemos recorrer diccionarios
dic = {'k1':'v1','k2':'v2','k3':'v3'}

for item in dic: #En este caso item tomara el valor de las keys del diccionario
    print(item)

for item in dic.values(): #Aqui item tomara el valor de los values en el diccionario
    print(item)

for item in dic.items(): #Y en este caso item tomara el key:value completo
    print(item)

for a,b in dic.items(): #Por ultimo, podemos utilizar variable separadas para obtener key:value de cada item
    print(a,b)

print()