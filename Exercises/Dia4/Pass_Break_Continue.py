#------------PASS---------------
#Tenemos un while declarado, pero sin dódigo definido.
#Sabemos que despues de esto tenemos que imprimir algo, para probar esto utilizamos pass

respuesta = ''
while respuesta == 's':
    pass #Pass permite que se ejecute el programa sin errores cuando nos falta código
         #Si no lo hubieramos puesto aquí, el compilador no ejecutaria el siguiente print y daria error de sintaxys

print("El pass funcionó") #Debido al pass podemos ver en consola la ejecución de este print

#------------BREAK---------------
#Tenemos un programa que imprime las letras de un nombre
#Pero si encuentra una R termina la ejecución DEL LOOP con break
nombre = input("Cual es tu nombre? \n")

for letra in nombre:
    if letra == 'r':
        print("Loop finalizado por break")
        break
    else:
        print(letra)
print("Validamos que el programa continua y solo se detuvo el loop")

#------------CONTINUE---------------
#Tenemos un programa que imprime las letras de un nombre
#Pero si encuentra una R termina la ejecución DE LA ITERACIÓN con continue
nombre = input("Cual es tu nombre? \n")

for letra in nombre:
    if letra == 'r':
        print("Es una r, salta la letra")
        continue
    else:
        print(letra)
print("Validamos que el programa continua y solo se detuvo el loop")