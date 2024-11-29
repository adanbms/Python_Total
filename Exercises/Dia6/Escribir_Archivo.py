#Solo leectura (no se puede escribir)
doc = open('prueba.txt', 'r')
print(doc.read())
doc.close()

#Escritura con reset (no se puede leer), el archivo se sobreescribe
doc = open('prueba.txt', 'w')

doc.write('something\n') #Salto de linea explicito en documento
doc.write('something2\n')

doc.write('''Asi podemos
escribir en varias lineas
sin poner explicitamente 
el salto de linea''') #Salto de linea en texto

doc.writelines(['\nhola','mundo','estoy','escribiendo','un','archivo']) #Este method solo concatena palabras (sin agregar espacios) y las escribe en una sola linea
doc.close()

#Escritura con append
doc = open('prueba.txt', 'a') #El archivo conserva su contenido y comezamos a escibir desde la ultima linea
lista = ['hola','mundo','estoy','escribiendo','un','archivo']

for i in lista:
    doc.writelines('\n' + i) #Escribimos una linea por palabra

doc.close()