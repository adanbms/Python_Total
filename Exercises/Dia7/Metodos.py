class Pajaro:
    #Atributo de clase
    alas = True

    #Atributos de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    '''
    Cuando escribimos métodos dentro de una clase 'self' es obligatorio como primer parametro del mismo, 
    aun si no necesitamos más parametros.
    
    En este mét0to piar hacemos referencia al atributo color
    cada que hagmos referencia a un atributo debemos indicar 'self' para indicar que es el valor de instancia al que nos referimos.
    Esto es incluso para los atributos de clase.
    '''
    def piar(self):
        print(f'pio, mi color es {self.color}')

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')

piolin = Pajaro('amarillo', 'canario')

'''Al igual que los atributos podemos hacer uso de los mét0dos'''
piolin.piar()
piolin.volar(56)