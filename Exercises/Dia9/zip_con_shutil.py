import shutil

'''
Shutil también puede swer utilizado para comprimir archivos
en este caso puede ser una ruta entera a comprimir
para ello necesitamos definir 3 cosas:
1. Ruta del archivo o carpeta a comprimir
2. Nombre del archivo comprimido
3. Indicar extension/formato zip en el método make_archive()

**Los archivos los encontraremos en nuestra ruta de trabajo al momento de ejecutar
'''
ruta_o_archivo_a_comprimir = 'D:\\Documents\\Proyectos\\Pycharm IDE\\Python_Total\\Exercises\\Dia6'
nombre_zip = 'Dia6_comprimido'
shutil.make_archive(nombre_zip, 'zip', ruta_o_archivo_a_comprimir)


'''
De la misma manera para descomprimir debemos indicar:
1. Nombre del archivo a descomprimir
2. Asignar un nombre de carpeta en donde queremos que quede la descompresión
3. El formati zip, sin punto

'''
shutil.unpack_archive('Dia6_comprimido.zip', 'Extracción_Dia6_comprimido', 'zip')