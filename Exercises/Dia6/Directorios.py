import os

#Get current working directory o obtener la ruta del directorio donde se ejecuta el programa
ruta = os.getcwd()
print(ruta) #D:\Documents\Proyectos\Pycharm IDE\Python_Total\Exercises\Dia6

#Establecer un directorio de trabajo diferente a donde se ejecuta la clase
#Para poder utilizar archivos en esa solo con su nombre
os.chdir('D:\\Users\\ASUS\\Desktop') #Windows
os.chdir('d/Users/ASUS/Desktop') #Mac/Linux

doc = open('archivo.txt')#Accedemos a un archivo en esa ruta
print(doc.read())
doc.close()

#Crear directorios en una ruta especifica
os.mkdir('D:\\Users\\ASUS\\Desktop\\prueba')

#Obtener partes de una ruta
ruta = 'D:\\Documents\\Proyectos\\Pycharm IDE\\newPythonProject\\Exercises\\Dia6\\prueba.txt'
elemento = os.path.basename(ruta)#prueba.txt - nombre archivo
elemento = os.path.dirname(ruta)#D:\\Documents\\Proyectos\\Pycharm IDE\\Python_Total\\Exercises\\Dia6 - nombre de ruta
elemento = os.path.split(ruta)#('D:\\Documents\\Proyectos\\Pycharm IDE\\Python_Total\\Exercises\\Dia6', 'prueba.txt') - tupla con elementos separados

#Eliminar carpetas
os.rmdir('D:\\Users\\ASUS\\Desktop\\prueba') #Elimina la carpeta 'prueba'

#-----------------PATH-----------------
#Accediendo a archivos sin importar la forma en que el OS genera las rutas
from pathlib import Path
carpeta = Path('C:/Users/ASUS/Desktop') #Al usar Path cualquier OS podra interpretarlo
archivo = carpeta/'otro_archivo.txt'
doc = open(archivo)#Accedemos a un archivo en esa ruta
print(doc.read())
doc.close()
