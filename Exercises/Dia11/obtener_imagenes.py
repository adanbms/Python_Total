import re
import bs4
import requests

#Hacemos un GET a la página que queremos hacer web_scraping
resultado = requests.get('https://escueladirecta-blog.blogspot.com')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.post-wrapper style')

n=0
for imagen in imagenes:
    n += 1
    #Despejar url de imagen
    url = imagen.text.replace('\\','').replace('%20',' ')
    url = re.sub(r'\s{14}\.\w{4}-\w{5}-\d{17,20}\s\{background-image:url\(','', url)
    url = url.replace('.png);}', '.png')
    print(url)

    #Obtener binario de esa imagen haciendo GET al URL
    binario_imagen = requests.get(url)

    #Crear archivo binario de imagen y guardar
    img = open(f'img/web_image{n}.jpg', 'wb') #wb = escribir binario
    img.write(binario_imagen.content)
    img.close()