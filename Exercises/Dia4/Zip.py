nombres = ["Ana","Hugo","Valeria"]
edades = [69,28,45]
ciudades = ["Lima","Madrid","Mexico"]


combinados = list(zip(nombres, edades, ciudades)) #Asi combinamos las listas
#Se asigna el elemento en la posición 0 de la primera lista al de la posición 0 de la segunda, y así sucesivamente.
print(combinados) #[('Ana', 69, 'Lima'), ('Hugo', 28, 'Madrid'), ('Valeria', 45, 'Mexico')]
#Si una de las listas tiene más elementos que la otra, el tuple tendrá el tamaño de la lista más corta y el elemento sobrante no se asignará, ni será parte de la lista de combinados.

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")