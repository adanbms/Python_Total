import os
import re
import time
import math
import datetime
from pathlib import Path

def fecha_hoy_con_formato():
    fecha = datetime.date.today()
    fecha = fecha.strftime("%d/%m/%Y")
    return fecha

def validar_formato(texto):
    coincidencia = re.search(r'N\w{3}-\d{5}', texto)
    if coincidencia != None:
        return coincidencia
    else:
        return False

def buscar_en_arbol(ruta):
    coincidencias = []
    for carpeta, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo != None:
                file = open(Path(carpeta,archivo), 'r')
                lines = file.readlines()
                for line in lines:
                    resultado = validar_formato(line)
                    if resultado != False:
                        coincidencias.append([Path(file.name).name, resultado.group()])
                    else:
                        pass
                file.close()
            else:
                pass
    return coincidencias

def imprimir_coincidencias(coincidencias):
    if len(coincidencias) > 0:
        print('ARCHIVO\t\t\t\tNRO. SERIE')
        print('-------\t\t\t\t----------')
        for coincidencia in coincidencias:
            print(f'{coincidencia[0]}\t\t{coincidencia[1]}')
    else:
        print('NO SE ENCONTRARON COINCIDENCIAS EN NINGUN ARCHIVO')

def inicio():
    print('----------------------------------------------------')
    print(f'Fecha de búsqueda: {fecha_hoy_con_formato()}')
    tiempo_inicio = time.time()
    ruta = 'D:\\Documents\\Proyectos\\Pycharm IDE\\Python_Total\\Exercises\\Dia9\\Proyecto+Dia+9\\Mi_Gran_Directorio'
    coincidencias = buscar_en_arbol(ruta)
    imprimir_coincidencias(coincidencias)
    tiempo_final = time.time()
    tiempo_total = math.ceil(tiempo_final - tiempo_inicio)

    print(f'Números encontrados: {len(coincidencias)}')
    print(f'Duración de la búsqueda: {tiempo_total} segundos')
    print('----------------------------------------------------')

inicio()
