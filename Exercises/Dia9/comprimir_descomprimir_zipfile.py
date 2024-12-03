import os
import zipfile

def eliminar_files():
    try:
        os.remove('Mi_texto_A.txt')
        os.remove('Mi_texto_B.txt')
        print('Archivos eliminados con éxito')
    except:
        print('Archivos no encontrados')


'''
Podemos utilizar este modulo para crear archivos comprimidos
escribirendo uno a uno
'''
#(nombre_final_de_archivo, metodo_de_escritura)
print('Creando comprimido.zip...')
mi_zip = zipfile.ZipFile('comprimido.zip', 'w')

mi_zip.write('Mi_texto_A.txt')
mi_zip.write('Mi_texto_B.txt')

mi_zip.close()

eliminar_files()

'''
De la misma forma podemos hacer la descompresion de uno a uno
o todos con estos comandos:
'''
#Abrimos el archivo en modo leectura
open_zip = zipfile.ZipFile('comprimido.zip', 'r')
print('Descomprimiendo archivos...')
open_zip.extractall() #Descomprimimos los archivos
