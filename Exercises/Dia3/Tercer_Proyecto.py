#Analizador de textos
print("--#-------------------- ANALIZADOR DE TEXTOS ------------------#--")

#Usuario ingresa texto
texto = input("Ingresa el texto a Analizar: \n")
#Pedimos 3 letras
letra1 = input("Ingresa la primera letra:\n")
letra2 = input("Ingresa la segunda letra:\n")
letra3 = input("Ingresa la tercera letra:\n")


#procesaremos esta informacion con 5 tipos de analisis y devolveremos
#1. Cuantas veces aparece cada letra que nos dieron en mayusculas o minusculas (Almacenaremos string en lista)
n = texto.upper().count(letra1.upper())
print(f"\nLa letra {letra1} aparece {n} veces en el texto")
n = texto.upper().count(letra2.upper())
print(f"La letra {letra2} aparece {n} veces en el texto")
n = texto.upper().count(letra3.upper())
print(f"La letra {letra3} aparece {n} veces en el texto")


#2. Cuantas palabras tiene el texto
palabras = texto.split(" ")
print("\nTu texto tiene {} palabras".format(len(palabras)))


#3. Cual es la primer letra y ultima letra del texto
print("\nLa primer letra de tu texto es: {}".format(texto[0]))
print("La ultima letra de tu texto es: {}".format(texto[len(texto)-1]))


#4. Devolveremos texto a la inversa
print("\nTu texto escrito a la inversa es el siguiente:\n\"{}\"".format(texto[::-1]))


#5. Si la palabra Python se encuentra dentro del texto (bools y diccionario para asociar true y false)
mi_bool = "PYTHON" in texto.upper()
dic = {True:'está presente en el texto', False:'no está presente en el texto'}
print("\nLa palabra python {}".format(dic[mi_bool]))
