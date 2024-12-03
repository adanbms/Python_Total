import os
import shutil
import send2trash

rootPath = os.getcwd() #Obtenemos el directorio donde este modulo se ubica

file = open('prueba.txt', 'w') #Creamos o sobreescribimos el archivp prueba.txt
file.write('Hole este es un texto de prueba para recordar el uso de os.getcwd() y file management en Python')
file.close()

#En la acrptea actual enlista los direcctorios existentes
print(os.listdir())

'''
--- shutil ---
Libreria muy util para:
- mover archivos -> move()

'''

#movemos prueba.txt a escritorio
shutil.move('prueba.txt', 'C:\\Users\\ASUS\\Desktop\\')

#removemos el contenido de una ruta por completo, files y directorios
#Ningun archivo de estos va a dar a la papeleria de reciclaje, t0do de pierde
try:
    shutil.rmtree('Aqui/pondiramos/una/ruta')
except:
    print('no se encontró la ruta')

'''
----- send2trash -----
En su lugar se recomienda usar send2trash para enviar los archivos directamente
a la papeleria de reciclaje del sistema y poderlos recuperar si es que se borra algo por error
instalar: pip install send2trash
'''

file = open('prueba2.txt', 'w') #Creamos o sobreescribimos el archivp prueba.txt
file.write('Hole este es un texto de prueba para recordar el uso de os.getcwd() y file management en Python')
file.close()

send2trash.send2trash('prueba2.txt') #envia el file a la papelera

'''
----- WALK -----
Camina por todos los directorios que encuentre dentro de la ruta que le proporcionemos.
Almacena 3 cosas en tuplas:
- La ruta en la que se encuentra
- Las subcarpetas que encuentre en esa ruta
- Los archivos que encuentre en esa ruta

**Solo se puede acceder a la información iterando sobre él
'''

ruta = 'D:\\Documents\\Proyectos\\Pycharm IDE\\Python_Total\\Exercises\\Dia6'

for carpeta, subcarpetas, archivos in os.walk(ruta):
    print(f'En la ruta: {ruta}')

    print('Las subcarpetas son: ')
    for subcarpeta in subcarpetas:
        print(f'\t{subcarpeta}')

    print('Los archivos son: ')
    for archivo in archivos:
        print(f'\t{archivo}')
        #Podemos utilizar esto para buscar archivos o carpetas que cumplan con ciertas caracteristicas
        #Y con ello facilitarnos el trabajao
        if archivo.startswith('E'):
            print('Encontramos un archivo que comienza con E')

    print('\n')