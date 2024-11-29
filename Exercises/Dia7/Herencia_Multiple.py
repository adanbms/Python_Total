class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('Ja Ja Ja')
    def hablar(self):
        print('Que tal!')

'''
Hijo hereda de las clases Padre y Madre respectivamente.

Vemos que tanto Padre como Madre cuentan con el método hablar
el método que se heredara a los hijos de estas clases es el que se encuentre primero
por método de resolución, es decir, de la primer clase que herede el hijo
En este caso, el método de la clase Padre

para tener claro el camino de resolucion de mátodos podemos ejecutar
print(Hijo.__mro__)
esto nos dara la jerarquia con la que Python buscará los métodos que indicamos cuando utilizamos un objeto
En este caso: (<class '__main__.Hijo'>, <class '__main__.Padre'>, <class '__main__.Madre'>, <class 'object'>)
 1. Buscará en Hijo
 2. Buscará en Padre
 3. Buscará en Madre
 
 Esto se extiende para Nieto
'''
class Hijo(Padre, Madre):
    pass

'''
A su vez Nieto hereda de las clases Hijo, Padre y Madre
ya que Hijo hereda las caracteristicas de sus padres
Es por ello que Nieto tiene acceso a los métodos hablar() y reir()
'''
class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()

print(Hijo.__mro__)