#Inmutables
nombre = "Carina" #Tenemos un string mal escrito
#nombre[0] = "K" #Intentamos cambiar el string pero esto nos daria error porque no son modificables internamente
#En su lugar lo que podemos hacer es auxiliarnos de funciones y variables para poder cambiar ese valor
#Opcion1
nombre = nombre.replace("C", "K")
#Opcion2
nombre = "Karina"

#Concatenables
n1 = "Kari"
n2 = "na"
print(n1+n2) #Karina
print(n1*3) #KariKariKari

#Multilineales
poema = """Mil pequeños peces blancos
comosi hirviera
el color del agua"""
print(poema)
#o
poema = "Mil pequeños peces blancos\ncomosi hirviera\nel color del agua"
print(poema)

#Verificamos si un caracter o palabra se encuentra o no en el Poema
print("agua" in poema) #true
print("anillo" in poema) #false
print("mamá" not in poema) #true
print("Mil" not in poema) #false

#Calculando longitud con len()
print(len(poema)) #55