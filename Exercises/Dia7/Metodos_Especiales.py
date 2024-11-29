class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones

    def __del__(self):
        print('Se ha eliminado el CD')

mi_cd = CD('Pink Floyd', 'The Wall', 24)

'''Al ser CD un objeto nuevo, creado por nosotos
tenemos que los métodos especiales como len() o str() 
no se comportan de la misma manera que como acostumbramos

Es aquí donde entran los metodos especiales, si queremos utilizar estos métodos
debemos definir en nuestras clases el comportamiento que queremos que tengan

Un ejemplo es cuando imprimimos nuestros objetos, en estos casos obtenemos una representación 
de la ubicación en memoria de este objeto:
- <__main__.CD object at 0x00000253D29DD5B0>

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

Podemos modificar el metodo __str__ para que cuando lo invoquemos se comporte de otra forma
- Album: The Wall de Pink Floyd

Lo mimo podemos hacer con todos los demás métodos
-del
-len
'''
print(mi_cd)
print(len(mi_cd))

del mi_cd #Elimina la instancia de un objeto en memoria