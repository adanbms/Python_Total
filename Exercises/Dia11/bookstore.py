import bs4
import requests

'''Definimos la base de los urls para cada página'''
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

'''Arreglo donde guardaremos la lista de libros de 4 y 5 estrellas'''
titulos_rating_alto = []

'''Iteraremos las 51 páginas de la bookstore'''
for pagina in range(1,51):
    #hacemos el llamado GET a la página n y lo hacemos lxml
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    '''Obtenemos los libros disponibles'''
    libros = sopa.select('.product_pod')

    '''Validamos la calificación de lso libros y agregamos el titulo a la lista si cumple'''
    for libro in libros:
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            titulo_libro = libro.select('a')[1]['title']
            titulos_rating_alto.append(titulo_libro)

'''imprimimos nuestra lista de titulos'''
for t in titulos_rating_alto:
    print(t)