x = 6
y = 2
z = 7

#Operaciones basicas (suma, resta multiplicación y división)
print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} entre {y} es igual a {x/y}")

#Redondeo hacia abajo o sin contar decimales (a//b)
print(f"{z} dividido al piso (redondeado hacia abajo) {y} es igual a {z//y}")

#Modulo o residuo de una división (a%b)
print(f"{z} modulo (residuo de una division) {y} es igual a {z%y}")

#Exponente (a**b)
print(f"{x} elevado a la {y} es igual a {x**y}")

#Raiz cuadrada o x elevado a 0.5 (x**0.5)
print(f"La raiz cuadrada de {x} es igual a {x**0.5}")

#Redondeo, hacia arriba a partir de 0.5 y hacia abajo cuando es menor a 0.5
#sin redondeo
print(90/7)
#redondeo sin decimales
print(round(90/7))
#redondeo utilizando solo 2 decimales
print(round(90/7,2))