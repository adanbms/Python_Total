import io
import pygame
import random
import math
from pygame import mixer

#Inicializamos Pygame
pygame.init()

#Abrimos pantalla del juego definiendo un ancho y un largo
pantalla = pygame.display.set_mode((800, 600))
#Mientras el programa se este ejecutando la pantalla estará abierta

#Titulo, icono y fondo imagen
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('iconos/ovni_2d.png')
pygame.display.set_icon(icono)
fondo_imagen = pygame.image.load('iconos/galaxy.jpg')

#agregar musica
mixer.music.load('sonidos/MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1) # -1 -> se reproduce cada que termina la canción

#Jugador (variables de posición e icono)
img_jugador = pygame.image.load('iconos/cohete.png')
jugador_x = 368
jugador_y = 500
#variable que guardará el cambio que se producira cada que presionesmo una tacla d emovimiento
jugador_x_cambio = 0

#Enemigos (variables de posición e icono)
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 5

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('iconos/ovni.png'))
    #Definimos que aparezca en una posición aleatoria dentro de la ventana con random
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    #variable que guardará el cambio que se producira cada que presionemos una tacla de movimiento
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(30)

#Bala (variables de posición e icono)
img_bala = pygame.image.load('iconos/bala.png')
bala_x = 0
bala_y = 500 #la posición del jugador en y
#variable que guardará el cambio que se producira cada que presionesmo una tacla d emovimiento
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False #No seha visible hasta que se invoque la función

#abrir fuente en bytes
def fuente_bytes(fuente):
    #Abre el .ttf en forma binaria
    with open (fuente, 'rb') as f:
        #lee todos los archivos y los almacena en una variable
        ttf_bytes = f.read()
    #Crea objeto BYTES a partir del TTF
    return io.BytesIO(ttf_bytes)

#Puntaje
puntaje = 0
# fuente = pygame.font.Font('freesansbold.ttf',32) #Unico tipo de fuente integrada a pygame y tamaño de letra
#Definiendo fuente externa:
fuente_como_bytes = fuente_bytes('fuente/towerruins.ttf')#tomandola en bytes para crear .exe
fuente = pygame.font.Font(fuente_como_bytes,32) #Unico tipo de fuente integrada a pygame y tamaño de letra
texto_x = 10
texto_y = 10

#definimos enemigo
def enemigo(x,y,n):
    pantalla.blit(img_enemigo[n], (x, y))

#definimos jugador en pantalla
def jugador(x,y):
    pantalla.blit(img_jugador, (x, y))

def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x+16, y+10))

#calcular distancia entre elementos y detectar colisión
def hay_colision(x1,y1,x2,y2):
    #formula de distancia entre 2 puntos algrebra lineal
    distancia = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1, 2))
    if distancia < 27:
        return True
    else:
        return False

#función para mostrar puntaje
def mostrar_puntaje(x, y):
    #render para crear texto en pantalla
    #(texto, antialias , color)
    texto = fuente.render(f'Puntaje: {puntaje}', True,(255,255,255))
    #hacemos blit, pero con el objeto construido
    pantalla.blit(texto, (x,y))

#TEXTO FINAL DEL JUEGO
fuente_final = pygame.font.Font(fuente_como_bytes, 50) #utiliza fuente como bytes
def texto_final():
    mi_fuente_final = fuente_final.render('GAME OVER', True, (255,255,255))
    pantalla.blit(mi_fuente_final, (250,200))


#Definimos loop de ejecución
se_ejecuta = True
while se_ejecuta:
    # Definir color de fondo RGB
    # pantalla.fill((205, 144, 228))
    
    #Definir fondo de pantalla con imagen
    pantalla.blit(fondo_imagen, (0,0))

    #iterar eventos
    for evento in pygame.event.get():
        #Validamos todos loe eventos y cuando el evento sea el boton (X) de cerrar, terminaremos el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #evento presionar tecla
        if evento.type == pygame.KEYDOWN:
            #Establecemos un cambio en el eje X si se presiona izquierda o derecha
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.6
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.6

            #si se presional la barra espaciadora
            if evento.key == pygame.K_SPACE:
                #no hacer cambios cuando ya se haya disparado una bala
                if not bala_visible:
                    #sonido de disparo
                    sonido_bala = mixer.Sound('sonidos/disparo.mp3')
                    sonido_bala.set_volume(0.3)
                    sonido_bala.play()
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        #Si se dejo de presionar un tecla
        if evento.type == pygame.KEYUP:
            #Si se deja de presionar izq o der dejamos de producir cambios en el eje X
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #A la posición del jugador le sumamos o restamos el cambio, para modificar su ubicacion
    jugador_x += jugador_x_cambio

    #mantener dentro de bordes de pantalla
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    #Cambiar posición enemigo
    for e in range(cantidad_enemigos):
        #fin del juego
        if enemigo_y[e] > 435:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]
    # mantener enemigos dentro de bordes de pantalla
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.6
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.6
            enemigo_y[e] += enemigo_y_cambio[e]

        # validar si hay colisión
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            #sonido colision
            colision_sonido = mixer.Sound('sonidos/Golpe.mp3')
            colision_sonido.set_volume(0.3)
            colision_sonido.play()

            # la bala regresa a su posición original y se hace invisible
            bala_y = 500
            bala_visible = False
            puntaje += 1  # aumentamos puntaje de jugador
            # Desaparece el enemigo y aparece uno nuevo en una posición random
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e],e)

    #movimiento bala al disparar
    if bala_y <= -64: #-64 porque es un poco despues del limite de pantalla
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio

    #actualizamos posición de jugador en ejecución
    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x, texto_y)

    #Actualizamos pantalla
    pygame.display.update()