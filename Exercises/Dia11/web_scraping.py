import bs4
import requests

#Hacemos un GET a la página que queremos hacer web_scraping
resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')

#La respuesta (el código) lo guardamos en una variable de beautiful soup para poder iterarlo
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#Obtiuene todos los elementos tilte como una lista
print(sopa.select('title'))
#Obtiene todos los elementos p  como una lista
print(sopa.select('p'))

#Obtener un elemento de la lista
print(sopa.select('title')[0]) #<title>Encapsulamiento - Pilares de la Programación Orientada a Objetos en Python</title>
#obtener solo el texto de un elemento de la lista
print(sopa.select('title')[0].text) #Encapsulamiento - Pilares de la Programación Orientada a Objetos en Python

#Obtener un parrafor en especifico
parrafo = sopa.select('p')[3].getText()
print(parrafo) #instancia + _ + NombreClase + mét0do/atributo oculto

#obtener columna lateral
columna_lateral = sopa.select('#PopularPosts1')
print('----------- columna_lateral ----------')

for p in columna_lateral:
    print(p.getText())