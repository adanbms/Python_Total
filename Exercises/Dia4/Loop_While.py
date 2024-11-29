monedas = 5

#Mientras monedas sea mayor a 0 ejecuta esto:
while monedas>0:
    print(f"Tengo {monedas} monedas")
    monedas-=1 #Con esto hacemos que las monedas se resten y en algun punto se cumpla la condición, sin esto el loop seria infinito
#tambien podemos utilizar else con while
else:
    print("No tengo más dinero")

#no sabemos cuantas iteraciones tendrá ya que la entrada del usuario lo define
respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir? s/n \n") #Si se ingresa una n termina el programa
else:
    print("Programa terminado") #Cuando se cumple la condiciónse ejecuta else