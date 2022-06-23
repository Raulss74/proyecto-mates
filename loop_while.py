numero = 10

while numero >= 0:
    print(numero)
    numero -= 1

print("------------")

numero2 = 50

while numero2 >= 0:
    if numero2 % 5 == 0:
        print(numero2)
    numero2 -= 1

print("-----------")

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)

