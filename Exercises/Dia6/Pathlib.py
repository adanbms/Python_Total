from pathlib import Path, PureWindowsPath

carpeta = Path('//Exercises/Dia6/prueba.txt')
#Ahora carpeta es un objeto Path, podemos utilizar sus metodos

#como leer archivos sin abrir y cerrar 'manualmente'
print(carpeta.read_text())
#ver el nombre del archivo
print(carpeta.name)
#obtener la extensión del archivo
print(carpeta.suffix)
#obtener el nombre sin extension
print(carpeta.stem)

#Validar si un archivo existe
if not carpeta.exists():
    print('El archivo no existe')
else:
    print('Genial! Existe...')


ruta_windows = PureWindowsPath(carpeta) #Transforma cualquier ruta en una ruta de Windows pura
print(ruta_windows)