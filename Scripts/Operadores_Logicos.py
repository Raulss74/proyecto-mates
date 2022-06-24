bool = not ('a' != 'a')
print(bool)

num1 = 36
num2 = 72/2
num3 = 48

test = num1 > num2 and num1 > num3
print(test)

test2 = num1 > num2 or num1 <num3
print(test2)

frase = "Cuando algo es lo suficientemente importante, " \
        "lo haces incluso si las probabilidades de que salga bien no te acompañan"

test3 = ("importante" in frase or "tecnología" in frase)
print(test3)
