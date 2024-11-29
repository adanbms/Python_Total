from random import randint
print("---#--------------------ADIVINA EL NUMERO--------------------#---")

number = randint(1,101)
player = input("¿Cuál es tu nombre?\n")
print(f"Hola {player}! ¿listo para jugar?\nEstoy pensado en un número entero entre 1 y 100 \n¿Qué número crees que es?\n(Tienes 8 intentos para adivinar)")

iteration = 1
while iteration<=8:
    player_number = int(input(f"Intento {iteration}: "))
    if player_number not in range(0,101):
        print("Has elejido un número que se encuentra fuera del rango mencionado (1-100)")
    elif player_number<number:
        print("Incorrecto, tu número es menor al número secreto")
    elif player_number>number:
        print("Incorrecto, tu número es mayor al número secreto")
    else:
        print("------------------------------------------------------------------------------------------------------")
        print(f"\t¡FELICIDADES!\nHas acertado en tu intento número {iteration}.\nEl número secreto era {number}...")
        print("------------------------------------------------------------------------------------------------------")
        break
    iteration += 1
else:
    print("------------------------------------------------------------------------------------------------------")
    print(f"Número de intentos excedido, el juego ha terminado.\n\tHAS PERDIDO :(\nEl número secreto era: {number}")
    print("------------------------------------------------------------------------------------------------------")

