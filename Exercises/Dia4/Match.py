serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe el producto")

#MATCH - la misma función que los if anteriores y el uso común
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe el producto")

#Casos distintos y valor agregado con python
cliente = {'nombre': 'Federico', 'edad': 45, 'ocupacion': 'instructor'}
pelicula = {'titulo': 'Matrix',
            'ficha_tecnica': {'protagonista': 'Keanu reeves',
            'director': 'Lana y Lilly Wachowski'}}
elementos = [cliente, pelicula, 'Libro']

for e in elementos: #para cada elemento en cliente
    match e:
        case {'nombre': nombre, #valida que si cumple con esta estructura es un cliente
            'edad': edad,
            'ocupacion': ocupacion}:
            print("Es un cliente")
            print (nombre, edad, ocupacion)
        case {'titulo': titulo, #valida que si cumple con esta estructura es una pelicula
            'ficha_tecnica': {'protagonista': protagonista,
                            'director': director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto") #Si no cumple con ninguna estructura va al default