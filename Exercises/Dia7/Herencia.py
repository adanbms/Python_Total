class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

class Pajaro(Animal):
    pass

print(Animal.__subclasses__()) #-> Dice que clases han heredado de esta clase
print(Pajaro.__bases__) #-> Dice de quien esta heredando

'''
Piolin es un objeto de tipo Pajaro, sin embargo como la clase Pajaro esta heredando de Animales
los métodos y atributos definidos en Animales son tambien parte de los Objetos de tipo Pajaro
espor ello que piolin puede acceder a los atributos color y edad, asi como al metodo nacer
aún cuando no esten definidos en la clase Pajaro

Además de esto cuando creamos una instancia del objeto Pajaro se nos piden atributos del constructor
de la clase Animales, con esto nos damos cuenta que si la clase hija no cuenta con constructor heredara el de la clase padre 
'''
piolin = Pajaro(2, 'amarillo')
piolin.nacer()
print(piolin.color)