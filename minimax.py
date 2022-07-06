menor = min(58,96,72, 25, 35)
print(menor)

mayor = max(58,96,72, 25, 35)
print(mayor)

lista = [58, 96, 72, 64, 25]
print(max(lista))
print(f"El número menor es {min(lista)} y el mayor es {max(lista)}")

nombres = ['juan', 'pablo', 'alicia', 'carlos']
print(min(nombres))
nombre = "Carlos"
print(min(nombre.lower()))
dic = {'C1':45, 'C2':11}
print(min(dic.values()))
print(max(dic.values()))

print("\n")
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(valor_maximo)

print("\n")
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = (max(lista_numeros) - min(lista_numeros))
print(rango)

print("\n")
dic = {"Carlos": 55, "Mari": 42, "Mabel": 78, "Jose": 44, "Lucas": 24, "Rocio": 35, "Sebastian": 19,
                      "Catalina": 2, "Dario": 49}

e_min = min(dic.values())
print(e_min)
u_name = max(dic)
print(u_name.lower())

print(f"La edad mínima es {e_min}; el último nombre es {u_name}.")


