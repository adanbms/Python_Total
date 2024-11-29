class Pajaro:
    '''
    def __init__ -> Se identifica como el mét0do constructor del objeto (asigna atributos)
                Cada que se requiera una instancia este mét0do constructor de Python verificará que se tengan todos los atributos necesarios apra crearlo
    (self, color) -> parametros que utiliza el met0do para construir el objeto
    self -> parametro OBLIGATORIO, significa 'él mismo'

    self.color = color
        self -> Representa instancia de cada uno de los objetos que se van a crear (puede ser cualquier palabra pero 'self' es una convención)
        self.color = color -> indica que al atributo color de esa instancia se le va a asignar un color que se envia como parametro al constructor
    '''
    def __init__(self, color):
        self.color = color

'''
Instanciamos un objeto de la clase Pajaro
    - Ya que definimos un atributo en esta clase llamado color, ahora es obligatorio pónerle un valor al crear un objeto/instancia
    - En este caso es el color negro
'''
mi_pajaro = Pajaro('negro')

'''
Este objeto pertenece al tipo Pajaro, y la clase pajaro cuenta con un atributo al que podemos acceder en todas sus instancias.
Tal como lo hacemos con str, num, etc..
En este caso ese atributo es color, por el momento, el valor de este será el que definimos al crear la instancia  
'''
print(mi_pajaro.color) # negro