import re

from Exercises.Dia3.Substrings import resultado

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

#Esto solo nos dice si está presente o no con booleanos
palabra = 'ayuda' in texto
print(palabra)

'''
re.search(patrón, texto)
Permite buscar un patrón dentro de una cadena de texto
y retorna un objeto con la información de la primer coincidencia. 
Si no hay nada retorna None
'''
patron = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span()) #Retorna la posición de inicio y final de la coincidencia
print(busqueda.end()) #Retorna final de la coincidencia
print(busqueda.start()) #Retorna inicio de la coincidencia
print(busqueda.group()) #Retorna la coincidencia


'''
re.findall(patrón, texto)
Encuentra todas las coincidencias del patrón dentro del texto
retorna una lista con los textos que coincidieron con el patrón
Si no hay nada retorna None

**No retorna datos de posición, ni nada extra, solo una lista con las coincidencias
'''
patron = 'ayuda'
busqueda = re.findall(patron, texto)
print(len(busqueda)) #Tamaño de la lista
print(busqueda) #Lista de coincidencias

'''
re.finditer(patrón, texto)
Itera la busqueda de un patrón dentro de un texto y retorna un objeto de resultados iterable
cada objeto dentro de este de resultados es similar al de re.search()
si no encuentra nada, regresa None
'''
patron = 'ayuda'
#Separandolo:
busqueda = re.finditer(patron, texto)
for coincidencia in busqueda:
    print(f'separado:{coincidencia.span()}')
#Haciendolo directo:
for coincidencia in re.finditer(patron, texto):
    print(f'directo:{coincidencia.span()}')


'''
---#-------------- PATRONES CON EXPRESIONES REGULARES --------------#---
'''

texto = 'llama al 545-865-6588 ya mismo o al 5697-789-854'

patron = r'\d\d\d-\d\d\d-\d\d\d\d'
resultado = re.search(patron, texto)
#Solo retornara un número ya que el otro no coincide con el patrón
print(f'ubicación:{resultado.span()}, coincidencia:{resultado.group()}') #ubicación:(9, 21), coincidencia:545-865-6588

#Otra forma de indicar el mismo patrón
patron = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron, texto)
print(f'ubicación:{resultado.span()}, coincidencia:{resultado.group()}') #ubicación:(9, 21), coincidencia:545-865-6588

#Podemos compilar un objeto de expresiones regulares en python agrupando estas expresiones y compilandolas en un objeto re
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron, texto)
#Esto nos da acceso al objeto particionado de tal forma que podemos acceder a cada parte de él
print(resultado.group(1)) #Comienza a contar desde 1
print(resultado.group(2)) #parte2
print(resultado.group(3)) #parte3

'''Validando contraseñas con search'''
clave = input('Clave: ')
patron = r'\D{1}\w{7}' #Contraseña que tenga 8 caracteres, inicie con una letra y contenga alfanumericos
checar = re.search(patron, clave)
print(checar)

'''
-----OPERADORES
'''
#OR
texto = 'No atendemos los lunes por la tarde'
buscar = re.search(r'lunes|martes', texto)
print(buscar) #Si encuentra lunes o martes imprimirá el resultado

#COMODIN
buscar = re.search(r'....demos', texto)
print(buscar) #Si encuentra texto seguido de 'demos' lo imprimira, como: atendemos

#INICIA CON
buscar = re.search(r'^\D', texto)
print(buscar) #Si el texto inicia con un NO digito imprimira

#TERMINA CON
buscar = re.search(r'\D$', texto)
print(buscar) #Si el texto termina con un NO digito imprimira

#Excluye
#Todas las letras que no sean un espacio vacio:
buscar = re.findall(r'[^\s]', texto)
print(buscar) #Lista de caracteres que no sean un espacio vacio

#Todas las palabras que no sean un espacio vacio:
buscar = re.findall(r'[^\s]+', texto)
print(buscar) #Lista de palabras que no son un espacio
print(''.join(buscar)) #Retorna el texto si espacios