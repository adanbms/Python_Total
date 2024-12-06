from tkinter import *
from tkinter import filedialog, messagebox
import random
import datetime

'''Funcionalidad de la calculadora'''
operador = ''

#Listas de precios para totales
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postre = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador #Para manipular una variable fuera de la función
    operador = operador + numero
    visor_calculadora.delete(0, END) #Limpia la pantalla de la calculadora
    visor_calculadora.insert(END, operador) #mostramos desde la derecha el operador seleccionado

def borrar_visor():
    global operador
    operador = '' #resetear operador para que al borrar empecemos desde 0
    visor_calculadora.delete(0, END) #borrar pantalla

def obtener_resultado(): #no trabaja con números negativos
    global operador
    resultado = str(eval(operador)) #Identifca la operación matematica en el string, la realiza y obtiene el resultado como un string
    visor_calculadora.delete(0, END)  # borrar pantalla
    visor_calculadora.insert(END, resultado) #ostramos resultado en pantalla
    operador = ''  # resetear operador para que al borrar empecemos desde 0

'''Activar y desactivar entradas validando los checkbox'''
def revisar_check():
    x = 0 #contador
    for c in cuadros_comida:
        if variables_comida[x].get() == 1: #si se activa el checkbox
            cuadros_comida[x].config(state=NORMAL) #Desbloqueamos el cuadro de entrada
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END) #limpiamos el 0
            cuadros_comida[x].focus() #Ponemos cursor en cuadro
        else: #en otro caso estará desactivado y lo pondremos en 0
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x+=1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1

'''Calculando totales'''
def total():
    sub_total_comida=0
    indice = 0
    for cantidad in texto_comida: #por cada elemento agregado a la lista de comida
        sub_total_comida = sub_total_comida + float(cantidad.get()) * precios_comida[indice] #sumaremos al subtotal la multiplicacipon de la cantidad del elemento por su precio
        indice+=1

    sub_total_bebida = 0
    indice = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + float(cantidad.get()) * precios_bebida[indice]
        indice += 1

    sub_total_postre = 0
    indice = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + float(cantidad.get()) * precios_postre[indice]
        indice += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre #obtenemos sub total
    impuestos = sub_total * 0.07 #calculamos impuestos
    total = sub_total + impuestos #obtenemos total

    #Asignamos los valores a las variables que se muestran en pantalla y redondeamos a 2 decimales
    var_costo_comida.set(f'$ {round(sub_total_comida,2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida,2)}')
    var_costo_postre.set(f'$ {round(sub_total_postre,2)}')
    var_subtotal.set(f'$ {round(sub_total,2)}')
    var_impuestos.set(f'$ {round(impuestos,2)}')
    var_total.set(f'$ {round(total,2)}')

'''Generando recibo de la cuenta'''
def recibo():
    texto_recibo.delete(1.0, END) #borramos el ticket anterior si es que existe
    num_recibo = f'N# - {random.randint(1000,9999)}' #Definimos un id random
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}' #damos formato a fecha
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n') #imprimios datos en recibo (END -> Inserta despues de la ultima linea escrita)
    texto_recibo.insert(END, f'*'*47 + '\n') #separador
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n') #cabeceras
    texto_recibo.insert(END, f'-'*47 + '\n')#separador

    # validar elementos selccionados por categoria comida, bebida y postre
    x = 0
    for comida in texto_comida:
        if comida.get() != '0': #si tiene checkbox activado
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                f'$ {int(comida.get()) * precios_comida[x]}\n') #insertalo al recibo despúes de la ultima entrada
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t'
                                     f'$ {int(postre.get()) * precios_postre[x]}\n')
        x += 1

    #Formateamos la impresion
    texto_recibo.insert(END, f'-' * 47 + '\n')  # separador
    texto_recibo.insert(END, f' Costo de la comida: \t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la bebida: \t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la postre: \t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 47 + '\n')  # separador
    texto_recibo.insert(END, f' Sub-total: \t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')  # separador
    texto_recibo.insert(END, f'Lo esperamos pronto!!!')  # separador

'''Guardar recibos'''
def guardar():
    info_recibo = texto_recibo.get(1.0, END) #obtenemostodo lo que haya en recibo de inicio(1.0) a fin (END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt') #Escribimos un archivo txt con la libreria filedialog
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información','Su recibo ha sido guardado.') #Despliega una ventana emergente con ese titulo y mensaje

'''Resetear'''
def resetear():
    texto_recibo.delete(0.1, END) #Borra el txto del recibo desde el comienzo hasta el final

    #Borramos las cantidades de cadaelemento del menu
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    #BLoqueamos las entradas de cada elemento del menú
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    #Limpiamos los checkbox
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    #Limpiamos variables de totales
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')


'''inicializamos tkinter'''
aplicacion = Tk()

'''
definir tamaño de pantalla

largo x ancho, puntox, puntoy (x,y donde aparecera la ventana inicialmente)
'''
aplicacion.geometry('1020x630+0+0')

'''
Definimos que la aplicación no sea maximizable, ni que se pueda cambiar el tamaño
para no afectar al diseño que tenemos
'''
aplicacion.resizable(0,0)

'''Poniendi titulo de ventana'''
aplicacion.title('Mi Restaurante - Sistema de Facturación')

'''Estableciendo color de fondo'''
aplicacion.config(bg='burlywood')


'''Diseñando panel superior'''
panel_superior = Frame(aplicacion, bd=1, relief=FLAT) #Establecemos ancho y tipo de relieve del frame(cuadro)
panel_superior.pack(side=TOP)#Establecemos posición en ventana
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4',
                        font=('Dosis',53), bg='burlywood', width=25) #establecemos en dónde se colocara la etiqueta y sus caracterisitcas
etiqueta_titulo.grid(row=0, column=0) #Esto porque es el unico elemento en el panel

'''Panel Menú (Izquierda)'''
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#Panel Costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_costos.pack(side=BOTTOM)

#Panel Comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comidas', font=('Dosis',19,'bold'),
                           bd=1, relief=FLAT, foreground='azure4')#Label frame = cuadro con etiqueta incorporada
panel_comidas.pack(side=LEFT)

#Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis',19,'bold'),
                           bd=1, relief=FLAT, foreground='azure4')#Label frame = cuadro con etiqueta incorporada
panel_bebidas.pack(side=LEFT)

#Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis',19,'bold'),
                           bd=1, relief=FLAT, foreground='azure4')#Label frame = cuadro con etiqueta incorporada
panel_postres.pack(side=LEFT)

'''Panel Derecho'''
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

#Panel calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack() #Al estar ocupada la parte de arriba, automaticamente se pone después y asi sucesivamente

#Panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

#Panel botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

#Lista de Productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua','soda','jugo','cola','vino1','vino2','cerveza1', 'cerveza2']
lista_postres = ['helado','fruta','brownies','flan','mousse','pastel1','pastel2','pastel3']

#generar items comida
variables_comida = []
cuadros_comida=[]
texto_comida=[]
contador = 0
for comida in lista_comidas:
    #crear check button
    variables_comida.append('') #agregar elemento vacio
    variables_comida[contador] = IntVar() #transformamos elemento en un integer
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador], #onvalue con check marcado, offvalue con check desmarcado, se guarda en variables_comida[contador]
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W) #Formaremos una fila en la columna 0 con el texto justificado del lado izquierdo (W)
    # crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar() #Haciendo string
    texto_comida[contador].set('0') #Estableciendo valor por defecto 0
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED, #Desactivado, no se puede escribir
                                     textvariable=texto_comida[contador]) #el texto se guardará en esta posición de la lista
    cuadros_comida[contador].grid(row=contador,
                                  column=1) #En la misma linea del check, pero columna 1
    contador += 1

#generar items bebida
variables_bebida = []
cuadros_bebida=[]
texto_bebida=[]
contador = 0
for bebida in lista_bebidas:
    #crear check button
    variables_bebida.append('') #agregar elemento vacio
    variables_bebida[contador] = IntVar() #transformamos elemento en un integer
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador], #onvalue con check marcado, offvalue con check desmarcado, se guarda en variables_bebida[contador]
                         command=revisar_check) #crearemos la función para validar el checkbuton
    bebida.grid(row=contador,
                column=0,
                sticky=W) #Formaremos una fila en la columna 0 con el texto justificado del lado izquierdo (W)
    # crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()  # Haciendo string
    texto_bebida[contador].set('0')  # Estableciendo valor por defecto 0
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED, #Desactivado, no se puede escribir
                                     textvariable=texto_bebida[contador]) #el texto se guardará en esta posición de la lista
    cuadros_bebida[contador].grid(row=contador,
                                  column=1) #En la misma linea del check, pero columna 1
    contador += 1

#generar items postre
variables_postre = []
cuadros_postre=[]
texto_postre=[]
contador = 0
for postre in lista_postres:
    #crear check button
    variables_postre.append('') #agregar elemento vacio
    variables_postre[contador] = IntVar() #transformamos elemento en un integer
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador], #onvalue con check marcado, offvalue con check desmarcado, se guarda en variables_postre[contador]
                         command=revisar_check)
    postre.grid(row=contador,
                column=0,
                sticky=W) #Formaremos una fila en la columna 0 con el texto justificado del lado izquierdo (W)
    # crear cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()  # Haciendo string
    texto_postre[contador].set('0')  # Estableciendo valor por defecto 0
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED, #Desactivado, no se puede escribir
                                     textvariable=texto_postre[contador]) #el texto se guardará en esta posición de la lista
    cuadros_postre[contador].grid(row=contador,
                                  column=1) #En la misma linea del check, pero columna 1
    contador += 1

#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

#Etiquetas de costos y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

#Etiquetas de costos y campos de entrada
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

#Etiquetas de costos y campos de entrada
etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0)
texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

#Etiquetas de costos y campos de entrada
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

#Etiquetas de costos y campos de entrada
etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuestos.grid(row=1, column=2)
texto_impuestos = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

#Etiquetas de costos y campos de entrada
etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

'''BOTONES'''
botones = ['total','recibo','guardar','resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 12, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=7)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

'''Area Recibo'''
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)

'''Calculadora'''
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          bd=1,
                          width=34)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=10) #columnspan = 4

botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','x','=','Borrar','0','/']

botones_guardados = []

fila=1
columna=0
#Acomodamos los botones en el espacio poe fila y columna en un loop para no hacerlo manualmente
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=5)
    botones_guardados.append(boton) #guardamos cada boton creado para poder interactuar con ellos
    boton.grid(row=fila,
               column=columna)

    if columna == 3:
        fila +=1

    columna+=1

    if columna == 4:
        columna = 0

#cada que se llame el boton mostraremos estos números en pantalla
botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado) #funcion
botones_guardados[13].config(command=borrar_visor) #funcion
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))


'''Hace que nuestra ventana no se cierre, es decir que la ejecución no finalice hasta que lo indiquemos'''
aplicacion.mainloop()