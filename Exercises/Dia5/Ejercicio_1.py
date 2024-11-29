#Numeros
def devolver_distintos(n1, n2, n3):
    suma = sum((n1,n2,n3))
    if suma>15:
        return max(n1,n2,n3)
    elif suma<10:
        return min(n1,n2,n3)
    elif 15>=suma>=10:
        num = suma - max(n1,n2,n3) - min(n1,n2,n3)
        return num

print(devolver_distintos(10,5,8))
print(devolver_distintos(2,5,1))
print(devolver_distintos(7,6,1))