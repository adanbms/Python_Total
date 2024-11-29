diccionario = {'c1':'valor1','c2':'valor2'}

print(type(diccionario)) #dict
print(diccionario)

#Consultar valores de claves
resultado = diccionario['c1']
print(resultado) #valor1

#Se pueden hacer diccionarios condistintos tipos de datos
cliente =  {'nombre':'Adan','apellido':'Bms','peso':88,'talla':1.76}
consulta = cliente['apellido'] #Así accedemos a las claves
print(consulta) #Bms

#Igualmente podemos tener diccionarios más complejos
dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
#para acceder a ello utilizamos la misma estructura de corchetes que hemos venido utilizando
#accederemos a un elemento del arreglo c2
print(dic['c2'][1]) #20
#O a un elemento dentro del diccionario en c3
print(dic['c3']['s1']) #100

#Ejercicio: Imprime la letra 'e' mayuscula
dic = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper()) #E

#Agregar y modificar elementos dentro del diccionario
dic = {1:'a',2:'b'} #Las key tambien pueden ser numeros enteros sin comillas
print(dic)
#agregamos elementos 3 y 4
dic[3] = 'c'
dic['d'] = 4
print(dic) #{1: 'a', 2: 'b', 3: 'c', 'd': 4}

#Modificamos el valor del elemento 2, por mayuscula
dic[2] = 'B'
print(dic) #{1: 'a', 2: 'B', 3: 'c', 'd': 4}

#PARA CONOCER TODAS LAS CLAVES O VALORES DENTRO PODEMOS UTILIZAR KEYS() y VALUES()
print(dic.keys()) # dict_keys([1, 2, 3, 'd'])
print(dic.values()) # dict_values(['a', 'B', 'c', 4])
print(dic.items())  #imprime lo que un dic tiene dentro: dict_items([(1, 'a'), (2, 'B'), (3, 'c'), ('d', 4)])