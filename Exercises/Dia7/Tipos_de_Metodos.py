class Pajaro:
    # Atributo de clase
    alas = True

    # Atributos de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    '''
    ---Metodos de Intancia---
    Son aquellos que afectan al self(valores y atributos de intancia)
    Pero tambien pueden modificar los atributos de Clase
    Así como el estado de la clase 
    
    - pintar_negro() -> Accede y modifica los atributos de instancia
    - volar() -> Accede a otros metodos
    - quitar_alas() -> Modifica el estado de la clase (u atributos de Clase)
    '''
    def piar(self):
        print(f'pio, mi color es {self.color}')

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    def quitar_alas(self):
        self.alas = False
        print('Ahora el pajaro no tiene alas')

    '''
    ---Metodos de Clase---
    Utilizan el decorador @classmethod en su definición
    Utilizan cls (la clase misma) como parametro y solo pueden acceder a atributos de clase.
    Los atributos de instancia no estan al alcance de estos métodos.
    Estos pueden ser llamados desde la clase sin necesidad de que exista una instancia de esta creada.
    '''
    @classmethod
    def poner_huevos(cls, cantidad):
        cls.alas = False
        print(f'El pajaro puso {cantidad} huevos y se quedo sin alas.')

    '''
    ---Metodos Estaticos---
    Utilizan el decorador @staticmethod en su definición
    no pueden accewder a ningun tipo de atributo, pero pueden recibir parametros externos
    También son accesibles sin una instancia del objeto
    '''
    @staticmethod
    def mirar():
        print('El pajaro mira')

piolin = Pajaro('amarillo', 'canario')

'''Metodos de Instancia'''
print(piolin.color) #amarillo
piolin.pintar_negro() #modifica atributos de instancia
print(piolin.color) #negro

piolin.volar(50) #accede a otros metodos, en este caso piar()

print(piolin.alas)
piolin.quitar_alas() #Cambia valores de atributos de clase
print(piolin.alas)

#Aunque siendo un atributo de clase podemos cambiar valores desde la instancia
piolin.alas = True
print(piolin.alas)

'''
-----Metodos de Clase-----
Solo modifica atributos de clase, en otros da error porque no recibe self(la instancia)
'''
print(piolin.alas)
Pajaro.poner_huevos(3)
print(piolin.alas)

'''Metodos Estaticos'''
Pajaro.mirar()