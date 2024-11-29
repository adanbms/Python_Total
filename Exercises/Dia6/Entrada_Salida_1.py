mi_archivo = open('prueba.txt') #Abrimos el archivo

print(mi_archivo) #No podemos acceder así al contenido, esto imprimirá: <_io.TextIOWrapper name='prueba.txt' mode='r' encoding='cp1252'>

print(mi_archivo.read()) #Debemos de leer el archivo para poder ver el contenido y utilizarlo

mi_archivo.close()
#-----------------------Ejemplo con reads
mi_archivo = open('prueba.txt')

print(mi_archivo.readline()) #Solo lee la primera linea del archivo
mi_archivo.readline() #Cada que se ejecuta el emthodo readline(), avanzamos una linea hacia abajo
print(mi_archivo.readline())#De tal forma que aqui obtendremos la tercera linea

mi_archivo.close() # cierra el archivo y libera el espacio en memoria que la leectura de este estaba utilizando.
#Recomendable siempre hacerlo asi

#-----------------------Ejemplo con for
mi_archivo = open('prueba.txt') #Abrimos el archivo

for l in mi_archivo:
    print(l) #Automaticamente hace referencia a las lineas del archivo.

mi_archivo.close()

#-----------------------Ejemplo con listas
mi_archivo = open('prueba.txt') #Abrimos el archivo
todas = mi_archivo.readlines() #Solo utilizar readlines con archivos pequeños ya que cada que ocupamos este se carga el archivo completo y podemos sobrecargar el sistema.
todas = todas.pop()
print(todas)
mi_archivo.close()