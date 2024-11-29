var1 = True
var2 = False

print(type(var1)) #Bool
print(var1)

#Asignando valor con condiciones
#Ejemplo1
numero = 5 > 2+3
print(type(numero)) #Bool
print(numero) #False

#Ejemplo 2
lista = [1,2,3,4]
control = 5 in lista
print(type(control)) #Bool
print(control) #False

#Función bool
#Es lo mismo que poner la condicion frente al igual, pero explicitamente
numero = bool(5>6)
print(numero)
#El valor por default de esta función es False, por lo que si llegamos a encontrarnosla así
numero = bool() #Significa que el valor es falso
print(numero)