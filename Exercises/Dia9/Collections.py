from collections import Counter, namedtuple

'''
Counter es un método de la libreria Collectiosn que nos permite 
contar la frecuencia con la que aparecen ciertos elementos dentro de un texto, un array o una lista
'''

#Para arrays cuenta frecuencia de elementos
numeros = [1,2,3,4,5,2,1,0,2,5,6,5,8,9,2,3,4,8]
#Contar cuantas veces aparece cada número dentro de la lista
print(Counter(numeros)) #Nos retorna en forma de tuplas con la estructura digito:frecuencia
# {2: 4, 5: 3, 1: 2, 3: 2, 4: 2, 8: 2, 0: 1, 6: 1, 9: 1}

#En el caso de strings cuenta frecuencia de caracteres
poema = '''Déjame reposar,
aflojar los músculos del corazón
y poner a dormitar el alma
para poder hablar,
para poder recordar estos días,
los más largos del tiempo'''

print(Counter(poema))

#Si queremos que cuente palabras podriamos:
print(Counter(poema.split( )))

#Podemos obtener el elemento que más se repite
print(Counter(poema).most_common(1))
#O los elementos que más se reiten
print(Counter(poema).most_common(2))


'''
Default dic: diccionario por defecto
'''
from collections import defaultdict

mid_dict = {'uno':'rojo', 'dos':'verde', 'tres':'negro'}
print(mid_dict['dos']) #Imprimiremos el valor de la clave dos: verde
#print(mid_dict['siete']) #Si tratamos de obtener el valor de una clave que no existe nos dara un error

'''
Para estos casos en los que la key no existe podemos utilizar defaultdict
 defaultdict(lambda: 'nada') -> Esta expresión significa que si se solicita un elemento que no existe
                                Se retornará y se le asignará el valor 'nada' con  la finalidad de que el programa no de error
'''
new_dic = defaultdict(lambda: 'nada')
new_dic['uno'] = 'Ejemplo'

print(new_dic['uno']) #Ejemplo
print(new_dic['dos']) #No existe, entonces retornará 'nada'

'''
Namedtuple: Permite genersr tuplas a las que podemos acceder a travez del nombre del atributo
    Es más como una forma rápida de generar objetos con namedtuple
'''

Persona = namedtuple('Persona', ['nombre','altura','peso'])
ariel = Persona('Ariel', 1.86, 96)
#Podemos acceder a la información de Ariel de diferentes maneras
#ya sea por nombre:
print(ariel.nombre)
print(ariel.altura)
print(ariel.peso)

#o por posición en la tupla
print(ariel[0]) #nombre
print(ariel[1]) #altura
print(ariel[2]) #peso