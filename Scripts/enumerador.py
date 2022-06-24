lista = ["a", "b", "c"]

for indice, item in enumerate(lista):
    print(indice, item)

print("\n")

for indice, item in enumerate(range(60, 71)):
    print(indice, item)

lizta = ["raul", "pepe", "carlos", "juanita"]
print("\n")
mis_tuples = list(enumerate(lizta))
print(mis_tuples)

print("\n")
print(mis_tuples[0][1])
print("\n")

lista_nombres = ["Marcos", "Laura", "Monica", "Javier", "Celina", "Marta", "Dario", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f"{nombre} se encuentra en el índice {indice}")

print("\n")

word = ["P", "y", "t", "h", "o", "n"]
lista_indices = list(enumerate(word))
print(lista_indices)

print("\n")

lista_nombres = ["Marcos", "Laura", "Monica", "Javier", "Celina", "Marta", "Dario", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    if (nombre[0] == "M"):
        print(indice, nombre)





