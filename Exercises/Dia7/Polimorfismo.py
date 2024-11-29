class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice muuu')


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')

'''
----- Polimorfismo -----
Hace referencia a que varios objetos pueden compartir el mismo nombre de método
aunque esten definidos de diferente forma.
En otras palabras es la capacidad de que los objetos puedan responder de manera diferente a un mismo mensaje o invocación.
Esto permite que podamos iterar sobre distintos tipos de objeto 
y llamar al método que comparten sin importar que sean diferentes
'''

#Vaca y oveja son diferentes objetos
vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

#Pero tienen el mismo mét0do hablar
vaca1.hablar()
oveja1.hablar()

#Teniendo en cuenta esto podemos iterar sobre ellos sin importar que sean diferentes
animales = [oveja1,vaca1]
for animal in animales:
    animal.hablar() #Nube dice beee #Aurora dice muuu

#Aplicandolo a algo más complejo podriamos construir funciones con ello
def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1) #Nube dice beee
animal_habla(vaca1) #Aurora dice muuu