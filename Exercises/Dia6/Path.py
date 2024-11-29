from pathlib import Path

#Construye una ruta a partir de strings
guia = Path('Barcelona','Sagrada_Familia.txt')
print(guia) #Barcelona\Sagrada_Familia.txt

base = Path.home() #Obtenemos la ruta absoluta a un usuario principal en la maquina
                   #En este caso: C:\Users\ASUS
guia = Path(base,'Barcelona','Sagrada_Familia.txt')#Path acepta cadenas y objetos de path para crear rutas
print(guia) #C:\Users\ASUS\Barcelona\Sagrada_Familia.txt

guia = Path(base,'Europa','España', Path('Barcelona','Sagrada_Familia.txt'))
print(guia) #C:\Users\ASUS\Europa\España\Barcelona\Sagrada_Familia.txt

#WITH NAME: Reemplaza el nombre del archivo en una ruta existente
guia2 = guia.with_name('La_Pedrera.txt')
print(guia2) #C:\Users\ASUS\Europa\España\Barcelona\La_Pedrera.txt

#Seleccionando una porcion del path
print(guia.parent) #C:\Users\ASUS\Europa\España\Barcelona
print(guia.parent.parent) #C:\Users\ASUS\Europa\España
print(guia.parent.parent.parent) #C:\Users\ASUS\Europa

#Enumerando archivos de una ruta especifica
guia = Path(Path().home(), 'Europa')
for txt in Path(guia).glob('*.txt'):
    print(txt)

#Enumerando archivos dentro de una estructura de carpetas dentro de Europa
guia = Path(Path().home(), 'Europa')
for txt in Path(guia).glob('**/*.txt'):
    print(txt)

#PATHS RELATIVOS: Generar un path a partir de un punto en una ruta
guia = Path('Europa','España','Barcelona','Sagrada_Familia.txt')

en_europa = guia.relative_to(Path('Europa'))
en_espania = guia.relative_to(Path('Europa','España'))

print(en_europa) #España\Barcelona\Sagrada_Familia.txt
print(en_espania) #Barcelona\Sagrada_Familia.txt