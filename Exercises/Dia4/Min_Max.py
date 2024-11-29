#VALORES NUMERICOS
menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)
print(menor)
print(mayor)

lista = [58,96,72,64,35]
print("El menor es "+str(min(lista))+" y el mayor es "+str(max(lista)))

#STRINGS
nombres = ["juan","pablo","alicia","carlos"]
print(min(nombres)) #alicia
nombre = "Carlos"
print(min(nombre)) #C, seria a pero busca primero en las mayusculas

#DICCIONARIOS
dic = {'C1':45, 'C2':11}
#obtener clave más baja:
print(min(dic))
#obtener valor más bajo:
print(min(dic.values()))
