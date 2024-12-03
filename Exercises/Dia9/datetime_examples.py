import datetime

'''TRABJANDO CON TIEMPO (HORAS)'''
#Establñecemos una hora definiendo (HH:mm:ss)
mi_hora = datetime.time(17,45,17)
#Una vez establecida la hora podremos acceder a cada elemento individualmente (horas,  minutos y segundos)
#Se utiliza el formato de 24h
print(mi_hora) #17:45:17
print(mi_hora.minute) #45

#Obtener hora actual
print(datetime.datetime.now().time()) #13:00:46.874504

'''TRABJANDO CON FECHAS (DIAS)'''
#Establecemos una fecha con YYYY-MM-dd
mi_dia = datetime.date(2024,12,8) #2024-12-08
#De la misma forma que el tiempo podemos acceder a cada elemento individualmente
print(mi_dia) #2024-12-08
print(mi_dia.day) #8
print(mi_dia.year) #2024
print(mi_dia.month) #12

#También podemos mostrar la fecha en otro formato con ctime
print(mi_dia.ctime()) #Sun Dec  8 00:00:00 2024 #no hay hora ya que solo establecimoas fecha
#Si no se establece un dato en la creación del tiempo o la fecha, este toma el valor de 0

#POdemos obtener el día actual
print(mi_dia.today())

'''TRABJANDO CON TODO FECHA Y HORA YYYY-MM-dd HH:mm:ss.SSSSSS'''
#Datetime cuenta con más parametros peropodemos omitirlos por ahora
mi_fecha = datetime.datetime(2024, 12, 8, 12,36,45,2500)
print(mi_fecha) #2024-12-08 12:36:45.002500

#podemos modificar los datos de esta fecha
mi_fecha = mi_fecha.replace(minute=35)
mi_fecha = mi_fecha.replace(hour=22)
mi_fecha = mi_fecha.replace(year=2025)

print(mi_fecha) #2025-12-08 22:35:45.002500


'''HACIENDO OPERACIONES CON FECHAS Y HORAS'''
#Cuanto ha vivido una persona
nacimiento = datetime.date(1936, 9,25)
defuncion = datetime.date(2024, 12,31)

tiempo_vida = defuncion - nacimiento
print(tiempo_vida) #32239 days, 0:00:00

#Cuanto tiempo ha estado despierta una persona
desperto = datetime.datetime(2024,11,28,9,25,12)
durmio = datetime.datetime(2024,11,29,12,52,15)

vigilia = durmio - desperto
print(vigilia) #1 day, 3:27:03
