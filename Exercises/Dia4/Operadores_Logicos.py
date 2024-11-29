#AND - Si todas las condiciones son verdaderas, sera verdadero, si alguna no será Falso
from Exercises.Dia3.Metodos_String import texto

mi_bool = (55==55) and ("a"=="a") # T + T = True
print(mi_bool)
mi_bool = (55==50) and ("a"=="a") # F + T = False
print(mi_bool)
mi_bool = (55==55) and ("b"=="a") # T + F = False
print(mi_bool)
mi_bool = (55==50) and ("b"=="a") # F + F = False
print(mi_bool)

texto = 'esta frase es breve'
mi_bool = ('frase' in texto) and ('breve' in texto) #True

#OR - Si alguna de las condiciones es verdadera retornará True, solo si todas sus condiciones son falsas retornará False.
mi_bool = (55==55) or ("a"=="a") # T + T = True
print(mi_bool)
mi_bool = (55==50) or ("a"=="a") # F + T = True
print(mi_bool)
mi_bool = (55==55) or ("b"=="a") # T + F = True
print(mi_bool)
mi_bool = (55==50) or ("b"=="a") # F + F = False
print(mi_bool)

texto = 'esta frase es breve'
mi_bool = ('python' in texto) or ('breve' in texto) #True
mi_bool = ('python' in texto) or ('curso' in texto) #False

#NOT - Niega el resultado de una comparación, es decir si la comparación es True, devolvera False y viceversa
mi_bool = not('python' in texto) #Python no se encuentra en el texto por lo que la primer condicion regresará false
print(mi_bool) #sin embargo al negarla con un NOT el valor que obtendremos será TRUE

mi_bool = not('breve' in texto) #breve se encuentra, la primer condicion regresará True
print(mi_bool) #sin embargo al negarla con un NOT, obtendremos False