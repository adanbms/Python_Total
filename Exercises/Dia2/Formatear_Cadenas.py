color_auto = "Rojo"
matricula = 101859

#En este caso se agregan llaves dentro del texto para indicar que se sustituira por el valor de una variable
#A continuación ecribiremos la funcion format y la lista de datos en el orden que se sustituiran en la cadena
print("Mi auto es {} y de matricula {}" .format(color_auto, matricula))


#En este caso para que Python tome este string como una cadena literal debemos iniciar con una letra f fuera de las comillas
#Aqui seguimos utilizando llaves para delimitar los valores de variables, sin embargo en esta version
#utilizamos el nombre de la variable dentro de las llaves para indicar que su valor ira ahi. De esta forma nuestro código serámás legible.
print(f"Mi auto es {color_auto} y de matricula {matricula}")