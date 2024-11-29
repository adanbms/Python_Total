#Son aquellos operadores que podemos utilizar para comparar 2 valores y obtener un resultado se si esa validación es Verdadera o Falsa.

#Diferencias entre = e ==
variable = 'Contenido' #Siempre que utilizamos = nos referimos a una asignación, es decir dar el valor de la derecha al elemento de la izquierda
mi_bool = 10==25 #En el caso de == se utiliza para comparaciones, esta experesión está validando que el primer elemento sera igual al segundo en valor
                 #De ser así obtendremos un valor booleano con el resultado

#Comparando igualdad con ==
mi_bool = 5+5==18-8 #True
mi_bool = 100.0==100 #True
mi_bool = 'Blanco'=='Negro' #False
mi_bool = 'Blanco'=='blanco' #False
mi_bool = 'Blanco'.lower()=='blanco' #True

#Comparando diferencia con !=
mi_bool = 100!=100.0 #False
mi_bool = 100!=100.1 #True

#Comparando valores con <,>,<=,>=
mi_bool = 5<9 #True
mi_bool = 5>9 #False
mi_bool = 5<=5 #True
mi_bool = 5>=2 #True

#En algunos casos podemos hacer conparaciones con más de 2 elementos, pero es recomendable usar operadores logicos en este caso
mi_bool = 5<7<9 #True
print(mi_bool)