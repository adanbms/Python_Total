import bs4
import requests
'''
La web tiene un patron en los urls de cada página de libros
nos aprovecharemos de esto para poder recorrer todas las páginas
para ello creamos un string que indica que recibira datos y los formateara en la posicion {}
'''
pag_n_libros = 'https://books.toscrape.com/catalogue/page-{}.html'

'''Formateamos el número en en string y hacemos GET a la página'''
resultado = requests.get(pag_n_libros.format('1'))

'''Convertimos página en un objeto lxml con beautiful oup'''
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

'''Obtenemos los libros de la página n '''
libros = sopa.select('.product_pod')

'''del libro 0 obtenemos la propiedad 'title' de la segunda etiqueta <a>'''
ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)