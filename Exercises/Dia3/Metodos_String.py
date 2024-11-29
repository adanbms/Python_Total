texto = "Este es un texto de prueba"

#Upper - Reescribe cadena en mayusculas
resultado = texto.upper() #reescribe toda la cadena
print(resultado) # ESTE ES UN TEXTO DE PRUEBA
resultado = texto[2].upper() #escribe solo ese carcater en mayuscula
print(resultado) # T

#Lower - Reescribe la cadena en minusculas
resultado = texto.lower()
print(resultado) #este es un texto de prueba

#Split - separa elementos tomando un caracter como separador
#retorna una lista de strings
resultado = texto.split() #Utiliza espacio como caracter default
print(resultado) # ['Este', 'es', 'un', 'texto', 'de', 'prueba']
resultado = texto.split("t") #Hace split utilizando t
print(resultado) # ['Es', 'e es un ', 'ex', 'o de prueba']

#Join - Une varios string dentro de UNA LISTA utilizando un caracter como separador
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d]) #Aprender Python es genial
print(e)
f = "-".join([a,b,c,d]) #Aprender-Python-es-genial
print(f)

#Find - funciona de la misma forma que index
#sin embargo cuando este no encuentra el caracter en el string no regresa aun error, si no un -1
#de igual forma existe un rfind()
resultado = texto.find("s") # 1
print(resultado)
resultado = texto.find("#") #-1
print(resultado)

#Replace - busca un caracter o texto proveeido y lo reemplaza en toda la cadena
resultado = texto.replace("e", "x") #Estx xs un txxto dx pruxba
print(resultado)
resultado = texto.replace("Este", "El") #El es un texto de prueba
print(resultado)
