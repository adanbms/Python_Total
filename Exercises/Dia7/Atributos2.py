class Pajaro:

    '''
    Definimos un atributo llamado alas que pertenece al objeto y será el mismo para todas las instancias desde el comienzo.
    '''
    alas = True

    '''
    def __init__ -> Mét0do constructor del objeto (asigna atributos de instancia)
    (self, color, especie) -> parametros que utiliza el met0do para construir el objeto
    self -> parametro OBLIGATORIO, significa 'él mismo'

    self.color = color -> indica que al atributo color de esa instancia se le va a asignar un color que se envia como parametro al constructor
    self.especie = especie -> indica que al atributo especie de esa instancia se le va a asignar una especie que se envia como parametro al constructor
    '''
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

'''
Instanciamos un objeto de la clase Pajaro
    - Ya que definimos dos atributos en esta clase llamado color, ahora es obligatorio pónerles un valor al crear un objeto/instancia
    - En este caso es el color negro y la especie tucan
'''
mi_pajaro = Pajaro('negro', 'tucan')

'''
Este objeto pertenece al tipo Pajaro, y la clase pajaro cuenta con dos atributos a los que podemos acceder en todas sus instancias.
Tal como lo hacemos con str, num, etc..
'''
print(f'Mi pajaro es un {mi_pajaro.especie} y su color es {mi_pajaro.color}') # Utilizamos atributos de clase

print(Pajaro.alas) #Vemos que es el mismo para la clase -> True
print(mi_pajaro.alas) # y para el objeto/instancia -> True