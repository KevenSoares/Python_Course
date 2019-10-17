"""

float type

the separator os decimals is "."

"""

#  wrong

valor = 1, 44
print(valor)
print(type(valor))
#  right

valor = 1.44
print(valor)
print(type(valor))

#  atribute value for 2 variable

valor1, valor = 1, 44
print(valor)
print(valor1)

#  we can convert float into int
res = (int(valor))
print(res)
print(type(res))

#  we can work with imaginary numbers

num = 5j
print(type(num))
print(num ** 2)
