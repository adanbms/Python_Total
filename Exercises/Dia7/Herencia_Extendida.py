class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):

    '''
    Para agregar atributos podemos hacerlo de 2 formas

    1. La primera es definir un cosntructor propio de la clase hija
    y definir como es que queremos que se maneje cada atributo de la clase hija
    pero además agregar los atributos que necesitemos

        def __init__(self, edad, color, altura_vuelo):
        self.edad = edad+1  -> Ejemplo para demostrar que puede ser diferente a como se definio en la Clase Padre
        self.color = color+' obscuro' -> Ejemplo para demostrar que puede ser diferente a como se definio en la Clase Padre
        self.altura_vuelo = altura_vuelo

    2. La segunda forma es utlizar el contructor de la Clase Padre para los atributos que se comparten con super()
    y atributos nuevos al constructor de la clase hija.
    Seguimos recibiendo los parametros edad y color, pero en este caso los manejará el constructor de la clase padre

        def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo
    '''
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    '''Mét0do heredado modificado solo para Pajaro'''
    def hablar(self):
        print('pio')

    '''Mét0do nuevo de Pajaro'''
    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')

piolin = Pajaro(3, 'amarillo', 15)

'''Mét0do herdado'''
piolin.nacer()

'''Mét0do heredado modificado'''
piolin.hablar() #pio

'''Mét0do nuevo'''
piolin.volar(5)

'''
El objeto Animal pide el tercer atributo del constructor de Pajaro, porque es una instancia de Animal
Ahora contamos con 2 atributos heredados y 1 atributo nuevo en Pajaro
'''
mi_animal = Animal(5, 'negro')
mi_pajaro = Pajaro(2, 'rojo', 13)