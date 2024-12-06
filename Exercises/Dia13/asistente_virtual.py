import pyttsx3
#podemos agregar un alias a las librerias poniendo la palabra as
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

from Exercises.Dia3.Substrings import resultado

'''
----Transformar voz en texto----
Escuchara nuestro microfono y regresara lo dicho como texto
'''
def transformar_audio_en_texto():
    #almacenar recognizer en variable
    r = sr.Recognizer()
    #configurar microfono
    with sr.Microphone() as origen:
        #tiempo de espera para empezar a escuchar
        r.pause_treshold = 0.8
        #informar que comenzó la grabación
        print('Ya puedes hablar')
        #guardar audio del microfono origen
        audio = r.listen(origen)

        try:
            #Utilizar google para reconocimiento de voz en español de méxico
            pedido = r.recognize_google_cloud(audio, language='es-mx')

            #imprimir lo que pudo escuchar
            print('Dijiste: ' + pedido)
            return pedido
        except sr.UnknownValueError: #Valor no reconocido
            print('Ups, no entendi lo que dijisdte..')
            return 'sigo esperando'
        except sr.RequestError: #No pudo completar la busqueda/reconocimiento
            print('Ups, hay servicio..')
            return 'sigo esperando'
        except: #Error inesperado
            print('Ups, no algo ha salido mal..')
            return 'sigo esperando'

'''
----Función para que el asistente pueda hablar----
'''
def hablar(mensaje):

    #encender motor de pyttsx3
    engine = pyttsx3.init()

    #hacer que pronuncie mensaje
    engine.say(mensaje)
    engine.runAndWait()

#Función que informa el día de la semana
def pedir_dia():
    #obtenemos la fecha del día de hoy
    dia = datetime.date.today()
    # obtener que dia de al semana es esa fecha (por id 0=lunes, 1=martes, etc...)
    dia_semana = dia.weekday()

    #Diccionario para hacer relación de días de la semana
    dias_semana_nombre={0:'Lunes',
                     1: 'Martes',
                     2: 'Miércoles',
                     3: 'Jueves',
                     4: 'Viernes',
                     5: 'Sábado',
                     6: 'Domingo'}

    #Decir día de la semana
    hablar(f'Hoy es {dias_semana_nombre[dia_semana]}')

#Función para pedir la hora
def pedir_hora():
    #obtenemos hora actual
    hora = datetime.datetime.now()
    hablar(f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos')

#Función para saludo inicial
def saludo_inicial():
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    hablar(f'{momento}, soy Elena, tu asistente personal. Por favor dime en que te puedo ayudar.')

'''Función central (Centro de pedidos)'''
def pedir_cosas():
    #Lo primero será saludar
    saludo_inicial()

    comenzar = True
    while comenzar:
        #Activar micro y guardar entrada en un string
        pedido = transformar_audio_en_texto().lower()

        #Mientras se encuentren estas palabras Elena hara las acciones
        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo YouTube.')
            webbrowser.open('https://www.youtube.com') #Nos permite abrir webs desde el código
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com') #WebBrowser sirve para abrir páginas en el navegador
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'que hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido: #wikipedia sirve para consultar cosas directamente ahi
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es') #configurar idioma de wikipedia
            resultado = wikipedia.summary(pedido, sentences=1) #que busque nuestro pedido en wikipedia y nos devuelva el primer parrafo que encuentre
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido) #pywhatkit hace busquedas en internet directamente (google)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya empiezo a reproducirlo')
            pywhatkit.playonyt(pedido) #Tambien podemos reproducir un vide que encuentre de una busqueda directamente en youtube
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es')) #pyjokes es una base de datos de bromas en distintos idiomas, en este caso español
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1] #se quedará con la ultima palabra de la lista
            #definimos diccionario con los nombres de acciones que corresponden a la web
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada) #Yahoo Finance ayuda a encontrar información sobre este tema de una manera estructurada y fácil de manejar
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'El precio de la acción de {accion} es {precio_actual}')
            except:
                hablar('Perdón, pero no la he encontrado')
        elif 'adios' in pedido: #Cerramos el programa y terminamos ejecución del while con break
            hablar('Me voy a descansar, cualquier cosa me avisas.')
            break

#Iniciamos el programa desde la función principal
pedir_cosas()