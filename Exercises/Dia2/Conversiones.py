costo = input("Cual es el costo de un gansito?") #Input regresa un tipo de dato string
impuestos = 7.3
precio = float(costo) + impuestos #Para poder hacer la suma necesitamos convertir el tipo de dato de costo en float
print("El resultado de la suma es " + str(precio)) #Para poder imprimirlo debemos castear el valor a string, aunque no es lo ideal