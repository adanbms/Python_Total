#Cero repetido
def cero_repetido(*args):
    counter = 0
    for arg in args:
        if arg==0:
            counter += 1
        else:
            counter = 0

        if counter == 2:
            return True
    return False

print(cero_repetido(5,6,1,0,0,9,3,5))
print(cero_repetido(6,0,5,1,0,3,0,1))