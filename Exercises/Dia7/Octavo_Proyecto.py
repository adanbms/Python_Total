'''Operaciones en cuenta de banco'''
from os import system
from random import randint

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}\n    Número de Cuenta: {self.numero_cuenta}\n    Balance: ${self.balance}'

    def depositar(self, cantidad):
        self.balance = self.balance + cantidad

    def retirar(self, cantidad):
        self.balance = self.balance - cantidad

def crear_cliente():
    nombre = 'Adan'
    apellido = 'Merino'
    numero_cuenta = randint(90000000, 99999999)
    balance = randint(30000, 1200000)
    return Cliente(nombre, apellido, numero_cuenta, balance)

def inicio():
    cliente = crear_cliente()
    option = ''
    while option!='4':
        system('cls')
        option = input(f'''
    ------ BANCOMEX ------
    Bienvenido!
    {cliente}

    1. Consulta de Saldo
    2. Retiro
    3. Deposito
    4. Salir

    ingresa el numero de la opción que deseas: ''')
        match option:
            case '1':
                print(f'Tu saldo es de: ${cliente.balance}')
            case '2':
                cantidad = input('¿Que cantidad deseas retirar?')
                if int(cantidad)>cliente.balance:
                    print('No puedes retirar más dinero del que tienes.')
                else:
                    cliente.retirar(int(cantidad))
                    print(f'Dinero retirado con éxito! \n Tu nuevo saldo es: ${cliente.balance}')
            case '3':
                cantidad = input('¿Que cantidad deseas depositar?')
                cliente.depositar(int(cantidad))
                print(f'Dinero depositado con éxito! \n Tu nuevo saldo es: ${cliente.balance}')
            case '4':
                print('Saliendo del programa...')
            case _:
                print('Opción invalida, intenta de nuevo')

        input('Oprime ENTER para continuar.')

inicio()