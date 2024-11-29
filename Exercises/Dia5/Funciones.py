'''
#---Sintaxis---#
-def #Palabra que indica a Python que crearemos la definición de una función
-nombre_función #Lo definimos nosotros, siempre con minusculas y guiones bajos en lugar de espacios
-() #Parentesis en donde podemos o no pasar parametros
-: #Indica que el codigo que este tabulado debajo de esta definición es parte de la función
-Descripción del comportamiento #Comentarios de documentación encerrados entre 3 comillas simples
-codigo #Codigo que queremos que se ejecute cada que llamemos la función
'''

#-----EJEMPLO---
#Definición:
def imprimir_nombre(nombre):
	'''Función que imprime un nombre proveido como parametro'''
	print(f"El nombre es: {nombre}")

#Uso:
imprimir_nombre("Adan")