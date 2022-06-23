nombres = ['Ana', 'Hugo', 'Valeria', 'Carolina', 'Raúl']
edades = [65, 29, 42, 55, 48]
ciudades = ['Lima', 'Madrid', 'Paris', 'Bogotá', 'México']

combinados = list(zip(nombres, edades, ciudades))

print(combinados)

print("\n")

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

print("\n")

paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]

combo = list(zip(paises, capitales))

for pais, capital in combo:
    print(f"La capital de {pais} es {capital}.")

print("\n")

productos = ["iPhone", "M600", "TV HDV", "Cámara K700", "Cámara N-1000", "Raptor 77"]
marcas = ["Apple", "Samsung", "Sony", "Kodak", "Nikon", "Alcatel"]

junto = list(zip(productos, marcas))

for producto, marca in  junto:
    print(f"El producto llamado '{producto}' es de la marca {marca}.")

print("\n")

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]
portugues = ["um", "dois", "trais", "quatro", "cinco"]

numeros = list(zip(espaniol, ingles, portugues))

print(numeros)

