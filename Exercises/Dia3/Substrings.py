text = "Hola"
#Index  ||||
#Index  0123

#Hacemos referencia común a la letra a con la posición 3
letra_a = text[3]
print(letra_a)

text = "Hola"
#Index  ||||
#Index  0321 (NEGATIVOS)

#Hacemos referencia inversa a la letra a con la posición -1
letra_a = text[-1]
print(letra_a)

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a")
print(resultado) #En este caso resultado sera igual a 3 ya que es el primer caracter en el string

resultado = mi_texto.index("a", 11, 18)
print(resultado) # es este caso el resultado sera 17 ya que solo estamos buscando en la parte de " prueba" y la unica a es la final


#------------ SUBSTRINGS ------------#
mi_variable = "Esta palabra será extraida"
#index         ||||||||||||||||||||||||||
#index         01234567890123456789012345 (No pongo numeros de 2 digitos pero el index llega al 25)

#Para extraer substrings utilizamos la siguiente estructura
# nombre_variable[indice_inicial:indice_final]
# (El caracter en el indice final no se incluye en el substring)
print(mi_variable[5:12]) #Imprimimos "palabra"

#Podemos utilizar un 3er parametro que indica que los caracteres en el fragmento se seleccionaran por intervalos
# nombre_variable[indice_inicial:indice_final:intervalo]
print(mi_variable[5:12:1]) #seleccionara todos los caracteres, como  palabra
print(mi_variable[5:12:2]) #seleccionara cada 2 caracteres, es decir p l b a
print(mi_variable[5:12:3]) #seleccionara cada 3 caracteres, es decir p  a  a

#Si ponemos un número negativo se comporta de la misma forma, solo que invierte el oreden de las letras
#Es decir, si tenemos la frase "Esta palabra será extraida"
#Obtendremos la frase inversa  "adiartxe áres arbalap atsE"
print(mi_variable[::-1])
#Esto funciona con intervalos no cerrados, es decir solo cuando alguno o ambos parametros de indice faltan.
print(mi_variable[5::-1])
print(mi_variable[:12:-1])
print(mi_variable[5:12:-1]) #si lo cerramos así no funcionará
