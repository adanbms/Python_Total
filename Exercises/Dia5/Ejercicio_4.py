def contar_primos(num):
    lista = list(range(0,num+1))
    primos = 0
    for n in lista:
        # 0 y 1 no son primos por convención
        if n<2:
            pass
        elif n==2:
            primos += 1
        elif n%2==0:
            pass
        else:  # para numeros impares.
            list_residuo = []
            zeros = []
            for i in range(3, n + 1, 2):
                residuo = n % i
                list_residuo.append(residuo)
            for j in list_residuo:
                if j == 0:
                    zeros.append(j)
            if len(zeros) > 1:
                pass
            else:
                primos += 1
    return primos

print(contar_primos(55))