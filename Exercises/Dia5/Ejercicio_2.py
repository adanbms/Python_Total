#Letras únicas y ordenadas
def ordenar_letras(palabra):
    letras = [letra for letra in palabra]
    letras = set(letras)
    letras = list(letras)
    letras.sort()
    return letras

print(ordenar_letras('parangaricutirimicuaro'))