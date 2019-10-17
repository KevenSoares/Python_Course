"""
string type
Ex:
'uma string' '485' 'a' 'True'
"uma string" "485" "a" "True"
'''uma string''' '''485''' '''a''' '''True'''

name = "Keven Soares"
print(name)
print(type(name))

name = '''Keven Soares'''
print(name)
print(type(name))

name = 'Keven Soares'
print(name)
print(type(name))



name = "Keven's Lab"
print(name)
print(type(name))

name = 'Keven \nSoares'
print(name)
print(type(name))

"""

#  """uma string""" """485""" """a""" """True"""
#  name = """Keven
#  Soares
#  """
#  print(name)
#  print(type(name))
#  name = """Keven Soares"""
#  print(name)
#  print(type(name))
name = "keven soares"
print(name[0:5])
print(name[6:13])
print(name.split())
#  vai do primeiro ao ultimo elemento e inverte
print(name[::-1])
print(name.replace('k', 'V'))

