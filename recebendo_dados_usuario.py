#  Entrada
print("name?")
name = input()
print("age?")
age = input()
#  Processamento

name = name.title()

#  Saída
#  modern format:
print("{0} is now {1}" .format(name, age))
#  new format since 3.7.x version
print(f'{name} is {age}')
#  how to cast a variable
print(f'{name} was born on {2019 - int(age)}')
