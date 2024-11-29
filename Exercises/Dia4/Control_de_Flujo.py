#Verificar SI 10 es mayor a 9
if 10>9: #Si la condicion es true, entonces se ejecuta el codigo dentro
    print("Es correcto")

if 1>9: #Si la condicion es false, entonces no se ejecuta nada
    print("Es correcto")
else: #En este caso siempre que la condición del if no se cumpla se ejecutará el codigo dentro de else
    print("No se cumple la condición")

#Utilizando elif
mascota = "perro"

if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
else:
    print("No sé que animal tienes")

#Anidando IFs
edad = 18
calificacion = 9

if edad<18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("Eres adulto")