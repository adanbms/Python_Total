'''Importamos unittest y el modulo que probaremos'''
import unittest
import cambia_texto

class PruebaCambiaTexto(unittest.TestCase):
    '''
    las pruebas deben iniciar con la palabra test_
    si no no serán validas para el sistema
    '''
    def test_mayusculas(self): #Creamos test
        palabra = 'buen dia'
        resultado = cambia_texto.todo_mayusculas(palabra) #Enviamos un valor a la función
        self.assertEqual(resultado, 'BUEN DIA') #Validamos el resultado con assertEqual

'''Definimos un mét0do main que se ejecute con unittest, si no no funcionaria nuestra prueba'''
if __name__ == '__main__':
    unittest.main()