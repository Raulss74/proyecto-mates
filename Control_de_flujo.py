edad = 26
calificacion = 10

if edad >= 18:
    print("Eres adulto")
else:
    print("Eres menor de edad")
if calificacion >= 6:
    print("Has aprobado tu curso")
else:
    print("No has aprobado tu curso")


num1 = (input("Escribe el primer número: "))
num2 = (input("Escribe el segundo número: "))
print(f"El primer valor es: {num1}")
print(f"El segndo valor es: {num2}")
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} es igual que {num2}")

print("----------------------------------")

edad = 17
licencia = False

if (edad >= 18) and (licencia == True):
    print("Puede conducir")
elif (edad >= 18) and (licencia == False):
    print("No puedes conducir, necesitas contar con licencia")
elif (edad <= 18) and (licencia == True):
    print("No puedes conducir. Debes tener 18 años o más")
else:
    print("No puedes conducir. Debes tener 18 años y contar con licencia")

print("----------------------------------")

habla_ingles = True
sabe_python = True

if (habla_ingles == True) and (sabe_python == True):
    print("Cumples con los requisitos para postularte")
elif (habla_ingles == True) and (sabe_python == False):
    print("Para postularte, necesitas saber programar en Python")
elif(habla_ingles == False) and (sabe_python == True):
    print("Para postularte, neceesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python y tener "
          "conocimientos de inglés")



